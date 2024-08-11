from dataclasses import dataclass
import importlib
from typing import Any, Literal, TypedDict, Dict
from LIB.AppBase import AppBase
import json
from GLOBAL import GLOBAL


class Provider:
    class_name: str
    init_args: list
    call_args: list

    def __init__(self, class_name: str, init_args: list, call_args: list):
        self.class_name = class_name
        self.init_args = init_args
        self.call_args = call_args

    def __call__(self) -> str | None:
        class_var = self.__get_class_var()
        return class_var(*self.init_args)(*self.call_args)

    def __get_class_var(self):
        module_name = "Providers." + self.class_name
        module = importlib.import_module(module_name)
        return getattr(module, self.class_name)


class App:
    name: str
    providers: Dict[str, Provider]

    def __init__(self, name: str, providers: Dict[str, Provider]):
        self.name = name
        self.providers = providers

    def __call__(self):
        app = AppBase(self.name, self.providers)
        app.update()


class Apps:
    def __init__(self) -> None:
        self.apps: Dict[str, App] = {}
        self.read(GLOBAL.Paths.Files.AppsJson)

    def __getitem__(self, key: str) -> Any:
        return self.apps[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.apps[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.apps

    def __iter__(self):
        return iter(self.apps)

    def __len__(self) -> int:
        return len(self.apps)

    def keys(self):
        return self.apps.keys()

    def values(self):
        return self.apps.values()

    def items(self):
        return self.apps.items()

    def read(self, app_json: str) -> None:
        with open(app_json, "r") as file:
            apps = json.load(file)
        self.apps = {
            app: App(
                app,
                {
                    provider: Provider(
                        provider_info["class"],
                        provider_info["init_args"],
                        provider_info["call_args"],
                    )
                    for provider, provider_info in providers.items()
                },
            )
            for app, providers in apps.items()
        }
