import os
from pathlib import Path


class Directories:
    Script = Path(__file__).parent.parent
    Data = Script.parent / "Data"
    Apps = Data / "apps"
    Icons = Data / "icons"


class Files:
    Index = Directories.Data / "index.json"
    Log = Directories.Script / ".log"
    Config = Directories.Script / ".ini"
    AppsScript = Directories.Script / "apps.py"
    AppsJson = Directories.Script / "apps.json"
    NewAppBackup = Directories.Script / "new_app.pkl"
    NewProviderBackup = Directories.Script / "new_provider.pkl"
    Categories = Directories.Data / "categories.json"


class Paths:
    Directories = Directories
    Files = Files
