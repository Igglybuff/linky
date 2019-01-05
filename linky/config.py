import configparser
import sys
from pathlib import Path


class ConfigParser:

    def __init__(self, config, downloader):
        self.c = config
        self.dict = {}
        self.list = []
        self.downloader = downloader
        self.supported_clients = ['jdownloader', 'pyload']
        self.download_client = None

    def get_abs_path(self):
        config_file = Path(self.c)
        abs_path = str(config_file.resolve())
        return abs_path

    def get_config_dict(self):
        config = configparser.ConfigParser()
        config.read(self.get_abs_path())
        for section in config.sections():
            self.dict[section] = {}
            for key, val in config.items(section):
                self.dict[section][key] = val
        return self.dict

    def get_sections_list(self):
        config = configparser.ConfigParser()
        config.read(self.get_abs_path())
        for section in config.sections():
            self.list.append(section)
        return self.list

    def set_client(self):
        if str(self.downloader):
            self.download_client = self.find_client_config()
        elif str(self.downloader).lower() in self.supported_clients:
            self.download_client = self.downloader
        else:
            print('ERROR: No supported download clients specified.')
        return self.download_client

    def find_client_config(self):
        sections = self.get_sections_list()
        config = self.get_config_dict()
        non_default_downloaders = 0

        if len(sections) == 1:
            print('WARNING: Skipping searching for defaults and using ' + str(sections[0]).capitalize() + ' as your download client since it is the only one configured.')
            default_client = str(sections[0]).lower()
            return default_client
        elif len(sections) == 0:
            print('ERROR: There were no supported download clients specified in your linky.conf!')
            sys.exit(1)

        for section in sections:
            if section in self.supported_clients:
                print('INFO: ' + 'Found ' + section + ' in linky.conf.')
                if config[section]['default']:
                    default_flag = str(config[section]['default']).lower()
                    if default_flag == 'true':
                        print('INFO: ' + section + ' is set as the default download client!')
                        default_client = str(section)
                        return default_client
                    else:
                        print('ERROR: Found a "default = " line in your linky.conf but it is not set to "true".')
                        sys.exit(1)
                else:
                    non_default_downloaders += 1
                    print('WARNING: Found "' + section + '", a supported download client, but it is not set to default. Looking for more configured download clients...')
            else:
                if non_default_downloaders > 1:
                    print('ERROR: At least one download client was found in your configuration, but no default was set!')
                    sys.exit(1)
                else:
                    print('ERROR: Something went horribly wrong when looking in your linky.conf!')
                    sys.exit(1)

    def find_indexer_config(self):
        pass
