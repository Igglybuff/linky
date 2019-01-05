from .myjdownloader import Jdownloader
from .config import ConfigParser


class LinkPusher:

    default_client = ''

    def __init__(self, links, config, downloader):
        self.links = links
        self.config = config
        self.downloader = downloader
        self.sections = []
        self.supported_clients = ['jdownloader', 'pyload']
        self.download_client = ''

    def set_client(self):
        config = ConfigParser(self.config)
        self.sections = config.get_sections_list()
        if self.downloader == "not_specified":
            self.download_client = self.find_client_config()
        elif self.downloader in self.supported_clients:
            self.download_client = self.downloader
        else:
            print('ERROR: No supported download clients specified.')
        return self.download_client

    def find_client_config(self):
        for section in self.sections:
            if section in self.supported_clients:
                print('Found ' + section + ' in linky.conf.')
                if str(self.config[section]['default']).capitalize() == 'True':
                    self.default_client = str(section)
                else:
                    print('ERROR: Found supported download clients but a default has not been configured! Set default = true in your linky.conf or specify a client with --downloader.')
            else:
                print('ERROR: No supported download clients specified.')
        return self.default_client

    def push_to_jdownloader(self):
        jd = Jdownloader(self.links, self.config)
        jd.send_to_jdownloader()
