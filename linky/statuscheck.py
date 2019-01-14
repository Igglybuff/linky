from sys import exit


class StatusChecker:

    def __init__(self, config, download_client):
        self.config = config
        self.download_client = download_client

    def get_status(self, links=None, all_items=None):
        pass

    def get_jdownloader_status(self):
        pass

    def get_pyload_status(self):
        pass
