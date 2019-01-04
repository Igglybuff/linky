import configparser
from pathlib import Path


class ConfigParser:

    def __init__(self, config):
        self.c = config
        self.dict = {}

    def get_abs_path(self):
        config_file = Path(self.c)
        abs_path = str(config_file.resolve())
        return abs_path

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self.get_abs_path())
        for section in config.sections():
            self.dict[section] = {}
            for key, val in config.items(section):
                self.dict[section][key] = val
        return self.dict
