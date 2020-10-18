import configparser
from pathlib import Path

from click import ClickException, BadParameter

class Repository:
    def __init__(self, path):
        self.tree = Path(path)
        
        self.git = self.tree / ".git"

        if not self.git.is_dir():
            raise ClickException(f"{path} is not a repository!")

        self.config = configparser.ConfigParser()
        
        config_file = self.git / "config"

        if config_file.is_file():
                self.config.read([config_file])
        else:
            raise ClickException("Configuration file missing")

        version = int(self.config.get("core", "repositoryformatversion"))
        if version != 0:
            raise ClickException(f"Unsupported repositoryformatversion {version}")

    @staticmethod
    def default_config():
        config = configparser.ConfigParser()
        config.add_section("core")
        config.set("core", "repositoryformatversion", "0")
        config.set("core", "filemode", "false")
        config.set("core", "bare", "false")
        return config

    @classmethod
    def create(cls, path):
        path = Path(path)
        
        if path.is_dir() and any(path.iterdir()):
            raise ClickException("Not an empty directory!")

        git = path / ".git"
        (git / "branches").mkdir(parents=True)
        (git / "objects").mkdir(parents=True)
        (git / "refs" / "tags").mkdir(parents=True)
        (git / "refs" / "heads").mkdir(parents=True)

        with open(git / "description", "w") as f:
            f.write("Unnamed repository; edit this file 'description' to name the repository.\n")

        with open(git / "HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")

        with open(git / "config", "w") as f:
            cls.default_config().write(f)

        return cls(path)
