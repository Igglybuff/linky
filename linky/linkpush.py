from .myjdownloader import Jdownloader
from .log import error, info, warning


class LinkPusher:

    default_client = None

    def __init__(self, config, silence=False):
        self.config = config
        self.silence = silence

    def push_links(self, links, downloader):
        if str(downloader).lower() == 'jdownloader':
            self.push_to_jdownloader(links)
        elif str(downloader).lower() == 'pyload':
            self.push_to_pyload(links)
        else:
            error(False, 'Something went wrong pushing the link to your download client.')

    def push_to_jdownloader(self, links):
        jd = Jdownloader(links, self.config, self.silence)
        jd.check_config()
        jd.send_to_jdownloader()

    def push_to_pyload(self, links):
        error(False, 'pyLoad is not supported yet.')
