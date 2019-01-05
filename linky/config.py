import configparser
from sys import exit
from os.path import abspath


class ConfigParser:

    def __init__(self, config):
        self.c = abspath(config)
        self.dict = {}
        self.supported_clients = ['jdownloader', 'pyload']

    def get_config_dict(self):
        config = configparser.ConfigParser()
        config.read(self.c)
        for section in config.sections():
            self.dict[section] = {}
            for key, val in config.items(section):
                self.dict[section][key] = val
        return self.dict

    def get_sections(self):
        sections_list = []
        config = configparser.ConfigParser()
        config.read(self.c)
        for section in config.sections():
            sections_list.append(section)
        return sections_list

    def get_client(self, downloader):
        if downloader:
            downloader = str(downloader).lower()
            if str(downloader).lower() in self.supported_clients:
                return downloader
            else:
                print('ERROR: Provided download client is not supported.')
                exit(1)
        else:
            download_client = self.find_client_config()
            return download_client

    def find_client_config(self):
        sections = self.get_sections()
        config = self.get_config_dict()
        non_default_downloaders = 0

        if len(sections) == 1:
            # TODO: this will fail unless sections are prefixed
            print('WARNING: Skipping searching for defaults and using ' + str(sections[0]).capitalize() + ' as your download client since it is the only one configured.')
            default_client = str(sections[0]).lower()
            return default_client
        elif len(sections) == 0:
            print('ERROR: There were no supported download clients specified in ' + self.c)
            exit(1)

        for section in sections:
            if section in self.supported_clients:
                print('INFO: ' + 'Found ' + section + ' in ' + self.c)
                if config[section]['default']:
                    default_flag = str(config[section]['default']).lower()
                    if default_flag == 'true':
                        print('INFO: ' + section + ' is set as the default download client!')
                        default_client = str(section)
                        return default_client
                    else:
                        print('ERROR: Found a "default = " line in your linky.conf but it is not set to "true".')
                        exit(1)
                else:
                    non_default_downloaders += 1
                    print('WARNING: Found "' + section + '", a supported download client, but it is not set to default. Looking for more configured download clients...')
            else:
                if non_default_downloaders > 1:
                    print('ERROR: At least one download client was found in your configuration, but no default was set!')
                    exit(1)
                else:
                    print('ERROR: Something went horribly wrong when looking in your linky.conf!')
                    exit(1)

    def get_indexers(self, indexers):
        if not indexers:
            indexers = 'fmovies'
        indexers = indexers.lower()
        return indexers

    def find_indexer_config(self):
        pass