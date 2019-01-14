from sys import exit


class StatusChecker:

    def __init__(self, config, download_client):
        self.config = config
        self.download_client = download_client

    def get_status(self, links=None, all_items=None):
        if str(self.download_client).lower() == 'jdownloader':
            self.get_jdownloader_status(links)
        elif str(self.download_client).lower() == 'pyload':
            self.get_pyload_status(links)
        else:
            print('ERROR: Something went wrong checking the status of your link(s).')
            exit(1)

    def get_jdownloader_status(self, links):
        pass

    def get_pyload_status(self, links):
        pass
