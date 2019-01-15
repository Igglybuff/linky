import myjdapi
import json
from .log import error, info, warning


class Jdownloader:

    def __init__(self, links, config, silence=False):
        self.l = links
        self.c = config
        self.silence = silence
        self.email = self.c['client jdownloader']['email']
        self.password = self.c['client jdownloader']['password']
        self.device_id = self.c['client jdownloader']['device_id']

    def check_config(self):
        self.check_email_format()
        self.check_device_id_validity()
        self.check_password_exists()

    def check_email_format(self):
        # print('Jdownloader email: ' + self.email)
        pass

    def check_password_exists(self):
        # print('Jdownloader password: ' + self.password)
        pass

    def check_device_id_validity(self):
        # print('Jdownloader device_id: ' + self.device_id)
        pass

    def connect(self):
        info(self.silence, 'Connecting to my.jdownloader.org...')
        jd = myjdapi.Myjdapi()
        jd.connect(self.email, self.password)
        info(self.silence, 'Connected!')
        return jd

    def send_to_jdownloader(self):
        jd = self.connect()
        info(self.silence, 'Sending URL to JDownloader...')
        jd.get_device(device_id=self.device_id).linkgrabber.add_links([{"autostart": True, "links": self.l}])
        info(self.silence, 'Your link was sent to JDownloader successfully!')

    def check_link_status(self, link=None):
        jd = self.connect()
        info(self.silence, 'Fetching link(s) status...')
        link_status = jd.get_device(device_id=self.device_id).downloads.query_packages()
        print(json.dumps(link_status, indent=4, sort_keys=True))
