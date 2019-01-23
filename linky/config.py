import configparser
from os.path import abspath
from .log import info, error, warning


class ConfigParser:

    def __init__(self, config, silence):
        self.c = abspath(config)
        self.silence = silence
        self.dict = {}
        self.supported_items = {
            'client': ['jdownloader', 'pyload'],
            'indexer': ['fmovies', 'orion'],
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
                error(False, 'Provided download client is not supported.')
        else:
            download_client = self.find_default_config('client')
            return download_client

    def find_default_config(self, section_type):
        sections = self.get_sections(section_type)
        config = self.get_config_dict()
        non_defaults = 0

        if len(sections) == 1:
            warning(self.silence, 'Skipping searching for defaults and using {} as your {} since it is the only one configured.'.format(str(sections[0]).capitalize(), section_type))
            default = str(sections[0]).lower()
            return default
        elif len(sections) == 0:
            error(False, 'There were no {}s specified in {}'.format(section_type, self.c))

        for section in sections:
            if section in self.supported_items[section_type]:
                info(self.silence, 'Found {} in {}'.format(section, self.c))
                if 'default' in config['client {}'.format(section)]:
                    default_flag = str(config[section]['default']).lower()
                    if default_flag == 'true':
                        info(self.silence, '"{}" is set as the default {}!'.format(section, section_type))
                        default = section
                        return default
                    else:
                        error(False, 'Found a "default = " line in {} but it is not set to "true".'.format(self.c))
                else:
                    non_defaults += 1
                    warning(self.silence, 'Found "{}", a supported {}, but it is not set to default. Looking for additional {}s...'.format(section, section_type, section_type))
            else:
                if non_defaults > 1:
                    error(False, 'At least one {} was found in your configuration, but no default was set!'.format(section_type))
                else:
                    error(False, 'Something went horribly wrong when reading {} !'.format(self.c))

        error(False, 'Could not find any supported {}s.'.format(section_type))

    def get_indexers(self, indexers):
        if indexers:
            indexers = indexers.lower()
            if indexers.lower() in self.supported_items['indexer']:
                return indexers
            else:
                error(False, 'Provided indexer is not supported.')
        else:
            indexer = self.find_default_config('indexer')
            return indexer

    @staticmethod
    def split_list(comma_list):
        normal_list = [x.strip() for x in comma_list.split(',')]
        return normal_list
