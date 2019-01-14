from sys import exit
from .myjdownloader import Jdownloader


class StatusChecker:

    def __init__(self, config, download_client, silence=False):
        self.config = config
        self.download_client = download_client
        self.silence = silence

    def get_status(self, links=None, all_items=False):
        if str(self.download_client).lower() == 'jdownloader':
            self.get_jdownloader_status(links)
        elif str(self.download_client).lower() == 'pyload':
            self.get_pyload_status(links)
        else:
            print('ERROR: Something went wrong checking the status of your link(s).')
            exit(1)

    def get_jdownloader_status(self, links):
        jd = Jdownloader(links, self.config)
        jd.check_link_status(links)

    def get_pyload_status(self, links):
        pass
