from .myjdownloader import Jdownloader
from .config import ConfigParser


class LinkPusher:

    default_client = ''

    def __init__(self, links, config, downloader):
        self.links = links
        self.config = config
        self.downloader = downloader

    def set_client(self):
        supported_clients = ['jdownloader', 'pyload']
        config = ConfigParser(self.config)
        sections = config.get_sections_list()
        if self.downloader == "not_specified":
            for section in sections:
                if section in supported_clients:
                    print("Found " + section + " in linky.conf.")
                    if self.config[section]['default'] == 'true':
                        self.default_client = str(section)


    def push_to_jdownloader(self):
        jd = Jdownloader(self.links, self.config)
        jd.send_to_jdownloader()
