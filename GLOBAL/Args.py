from dataclasses import dataclass
import argparse
from typing import List, Optional


@dataclass
class Args:
    app: Optional[List[str]] = None
    github: bool = False
    virustotal: bool = False
    config: bool = False
    debug: bool = False
    xhost: bool = False
    new: bool = False

    @classmethod
    def parse_args(cls) -> "Args":
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--app", "--apps", nargs="+", help="App name")
        parser.add_argument(
            "-g", "--github", help="Force Github push", action="store_true"
        )
        parser.add_argument(
            "-v", "--virustotal", help="Force VirusTotal analysis", action="store_true"
        )
        parser.add_argument(
            "-c", "--config", help="Edit config file", action="store_true"
        )
        parser.add_argument("-d", "--debug", help="Debug mode", action="store_true")
        parser.add_argument(
            "-x", "--xhost", help="Use xhost: Display", action="store_true"
        )
        parser.add_argument("-n", "--new", help="Add new app", action="store_true")

        args = parser.parse_args()
        return cls(**vars(args))
