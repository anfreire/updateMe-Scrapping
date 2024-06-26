from typing import Literal, Dict, Tuple
import os
from lib.github import Github
from lib.apk import Apk
from lib.virustotal import VirusTotal
from GLOBAL import GLOBAL
from utils.Index import Index


class AppBase:
	def __init__(self, app_title: str, providers: Dict[str, callable]):
		self.app_title = app_title
		self.providers = providers
		GLOBAL.Log(f"Starting {self.app_title}", level="INFO")

	def make_file_name(self, provider_title: str) -> str:
		title = self.app_title.replace(" ", "_").lower()
		provider = provider_title.replace(" ", "_").lower()
		return f"{title}_{provider}.apk".replace("(", "").replace(")", "")

	def download(self, provider_title: str, fun: callable) -> str | None:
		path = None
		try:
			path = fun()
		except Exception as e:
			GLOBAL.Log(
				f"{self.app_title} - {provider_title}: update failed\n{str(e)}\n",
				level="ERROR",
				exception=True,
			)
			try:
				path = fun()
			except Exception as e:
				GLOBAL.Log(
					f"{self.app_title} - {provider_title}: update failed\n{str(e)}\n",
					level="CRITICAL",
					exception=True,
				)
		return path

	def move_file(self, path: str, provider_title: str) -> str:
		newFileName = os.path.join(
			GLOBAL.Paths.AppsDir, self.make_file_name(provider_title)
		)
		if os.path.exists(newFileName):
			os.remove(newFileName)
		os.rename(path, newFileName)
		return newFileName

	def parse_apk(self, path: str) -> Apk | None:
		try:
			return Apk(path)
		except Exception as e:
			GLOBAL.Log(
				f"Failed to parse {path}\n{str(e)}\n",
				level="ERROR",
				exception=True,
			)
			return None

	def process(self, provider_title: str, apk: Apk, path: str) -> None:
		oldProvider = Index.index[self.app_title]["providers"][provider_title]
		if apk.packageName != oldProvider["packageName"]:
			GLOBAL.Log(
				f"{self.app_title} - {provider_title} has different package name. Expected: {oldProvider['packageName']}, got: {apk.packageName}",
				level="CRITICAL",
			)
		forced = False
		if GLOBAL.Args.virustotal:
			VirusTotal.add(self.app_title, provider_title, path, apk.sha256)
			forced = True
		if GLOBAL.Args.github:
			download = Github.push_release(path)
			forced = True

		if oldProvider["sha256"] == apk.sha256 and not forced:
			GLOBAL.Log(
				f"{self.app_title} - {provider_title} is up to date",
				level="INFO",
			)
			return
		
		if not GLOBAL.Args.virustotal:
			VirusTotal.add(self.app_title, provider_title, path, apk.sha256)
		
		if not GLOBAL.Args.github:
			download = Github.push_release(path)

		Index.index[self.app_title]["providers"][provider_title]["packageName"] = apk.packageName
		Index.index[self.app_title]["providers"][provider_title]["download"] = download
		Index.index[self.app_title]["providers"][provider_title]["version"] = apk.version
		Index.index[self.app_title]["providers"][provider_title]["sha256"] = apk.sha256
		
		if forced:
			GLOBAL.Log(
				f"{self.app_title} - {provider_title} updated forcefully",
				level="INFO",
			)
		elif oldProvider["version"] < apk.version:
			GLOBAL.Log(
				f"{self.app_title} - {provider_title} updated from {oldProvider['version']} to {apk.version}",
				level="INFO",
			)
		else:
			GLOBAL.Log(
				f"{self.app_title} - {provider_title} got bug fix", level="INFO"
			)

	def update(self):
		for provider_title, fun in self.providers.items():
			GLOBAL.Log(f"Updating {self.app_title} - {provider_title}", level="INFO")
			path = self.download(provider_title, fun)
			if path is None:
				continue
			newFileName = self.move_file(path, provider_title)
			apk = self.parse_apk(newFileName)
			if apk is None:
				continue
			self.process(provider_title, apk, newFileName)
			Index.write()
