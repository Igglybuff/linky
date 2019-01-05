from .myjdownloader import Jdownloader


class LinkPusher:

    default_client = None

    def __init__(self, links, config, downloader):
        self.links = links
        self.config = config
        self.downloader = downloader

    def push_link(self):
        if str(self.downloader).lower() == 'jdownloader':
            self.push_to_jdownloader()
        elif str(self.downloader).lower() == 'pyload':
            self.push_to_pyload()
        else:
            print('ERROR: Something went wrong pushing the link to your download client.')
            sys.exit(1)

    def push_to_jdownloader(self):
        jd = Jdownloader(self.links, self.config)
        jd.check_config()
        jd.send_to_jdownloader()

    def push_to_pyload(self):
        pass
