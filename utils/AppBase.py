from typing import Dict
import os
from LIB.Github import Github
from LIB.Apk import Apk
from LIB.App import App
from GLOBAL import GLOBAL


class AppBase:
    def __init__(self, app_title: str, providers: Dict[str, callable]):
        self.app_title = app_title
        self.providers = providers
        GLOBAL.Log(f"Starting {self.app_title}", level="INFO")

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
            GLOBAL.Paths.Directories.Apps, App.filter_name(provider_title)
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
        oldProvider = GLOBAL.Index[self.app_title]["providers"][provider_title]
        if apk.packageName != oldProvider["packageName"]:
            GLOBAL.Log(
                f"{self.app_title} - {provider_title} has different package name. Expected: {oldProvider['packageName']}, got: {apk.packageName}",
                level="CRITICAL",
            )
        forced = GLOBAL.Args.virustotal or GLOBAL.Args.github
        if GLOBAL.Args.virustotal:
            previous = GLOBAL.VirusTotal.check_previous_submissions(path, apk.sha256)
            if previous is None:
                GLOBAL.VirusTotal.add(self.app_title, provider_title, path, apk.sha256)
            else:
                if previous:
                    GLOBAL.Log(
                        f"{self.app_title} - {provider_title} is infected",
                        level="CRITICAL",
                    )
                    GLOBAL.Index[self.app_title]["providers"][provider_title][
                        "safe"
                    ] = False
                    GLOBAL.Index.write()
                else:
                    GLOBAL.Log(
                        f"{self.app_title} - {provider_title} is safe",
                        level="INFO",
                    )
                    GLOBAL.Index[self.app_title]["providers"][provider_title][
                        "safe"
                    ] = True
                    GLOBAL.Index.write()
        if GLOBAL.Args.github:
            download = Github.push_release(path)

        if oldProvider["sha256"] == apk.sha256 and not forced:
            GLOBAL.Log(
                f"{self.app_title} - {provider_title} is up to date",
                level="INFO",
            )
            return

        if not forced and not GLOBAL.Args.virustotal:
            GLOBAL.VirusTotal.add(self.app_title, provider_title, path, apk.sha256)

        if not forced and not GLOBAL.Args.github:
            download = Github.push_release(path)

        GLOBAL.Index[self.app_title]["providers"][provider_title][
            "packageName"
        ] = apk.packageName
        GLOBAL.Index[self.app_title]["providers"][provider_title]["download"] = download
        GLOBAL.Index[self.app_title]["providers"][provider_title][
            "version"
        ] = apk.version
        GLOBAL.Index[self.app_title]["providers"][provider_title]["sha256"] = apk.sha256

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
            GLOBAL.Log(f"{self.app_title} - {provider_title} got bug fix", level="INFO")

    def update(self):
        for provider_title, fun in self.providers.items():
            GLOBAL.Log(f"Updating {self.app_title} - {provider_title}", level="INFO")
            path = self.download(provider_title, fun)
            if path is None:
                GLOBAL.Log(
                    f"{self.app_title} - {provider_title}: download failed",
                    level="CRITICAL",
                )
                continue
            newFileName = self.move_file(path, provider_title)
            apk = self.parse_apk(newFileName)
            if apk is None:
                GLOBAL.Log(
                    f"{self.app_title} - {provider_title}: parsing failed",
                    level="CRITICAL",
                )
                continue
            self.process(provider_title, apk, newFileName)
            GLOBAL.Index.write()
