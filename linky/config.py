import configparser
from sys import exit
from os.path import abspath


class ConfigParser:

    def __init__(self, config):
        self.c = abspath(config)
        self.dict = {}
        self.supported_items = {
            'client': ['jdownloader', 'pyload'],
            'indexer': ['fmovies'],
        }

    def get_config_dict(self):
        config = configparser.ConfigParser()
        config.read(self.c)

        for section in config.sections():
            self.dict[section] = {}
            for key, val in config.items(section):
                self.dict[section][key] = val
        return self.dict

    def get_sections(self, section_type='all'):
        sections_list = []
        config = configparser.ConfigParser()
        config.read(self.c)

        if section_type == 'all':
            prefix = ''
        else:
            prefix = section_type

        for section in config.sections():
            if section.startswith(prefix):
                sections_list.append(section[len(prefix + ' '):])

        return sections_list

    def get_client(self, downloader):
        if downloader:
            downloader = str(downloader).lower()
            if str(downloader).lower() in self.supported_items['client']:
                return downloader
            else:
                print('ERROR: Provided download client is not supported.')
                exit(1)
        else:
            download_client = self.find_default_config('client')
            return download_client

    def find_default_config(self, section_type):
        sections = self.get_sections(section_type)
        config = self.get_config_dict()
        non_defaults = 0

        if len(sections) == 1:
            print('WARNING: Skipping searching for defaults and using ' + str(sections[0]).capitalize() + ' as your ' +
                  section_type + ' since it is the only one configured.')
            default = str(sections[0]).lower()
            return default
        elif len(sections) == 0:
            print('ERROR: There were no ' + section_type + 's specified in ' + self.c)
            exit(1)

        for section in sections:
            if section in self.supported_items[section_type]:
                print('INFO: ' + 'Found ' + section + ' in ' + self.c)
                if config[section]['default']:
                    default_flag = str(config[section]['default']).lower()
                    if default_flag == 'true':
                        print('INFO: ' + section + ' is set as the default ' + section_type + '!')
                        default = section
                        return default
                    else:
                        print('ERROR: Found a "default = " line in ' + self.c + ' but it is not set to "true".')
                        exit(1)
                else:
                    non_defaults += 1
                    print('WARNING: Found "' + section + '", a supported ' + section_type +
                          ', but it is not set to default. Looking for additional ' + section_type + 's...')
            else:
                if non_defaults > 1:
                    print('ERROR: At least one ' + section_type +
                          ' was found in your configuration, but no default was set!')
                    exit(1)
                else:
                    print('ERROR: Something went horribly wrong when reading ' + self.c + '!')
                    exit(1)

    def get_indexers(self, indexers):
        if not indexers:
            indexers = 'fmovies'
        indexers = indexers.lower()
        return indexers

    def find_indexer_config(self):
        pass
