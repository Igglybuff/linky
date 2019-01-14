from sys import exit
from .myjdownloader import Jdownloader


class LinkPusher:

    default_client = None

    def __init__(self, config):
        self.config = config

    def push_links(self, links, downloader):
        if str(downloader).lower() == 'jdownloader':
            self.push_to_jdownloader(links)
        elif str(downloader).lower() == 'pyload':
            self.push_to_pyload(links)
        else:
            print('ERROR: Something went wrong pushing the link to your download client.')
            exit(1)

    def push_to_jdownloader(self, links):
        jd = Jdownloader(links, self.config)
        jd.check_config()
        jd.send_to_jdownloader()

    def push_to_pyload(self, links):
        print('ERROR: pyLoad is not supported yet.')
        exit(1)
