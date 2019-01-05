import myjdapi


class Jdownloader:

    def __init__(self, links, config):
        self.l = links
        self.c = config
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

    def send_to_jdownloader(self):
        print('INFO: ' + 'Connecting to my.jdownloader.org...')
        jd = myjdapi.Myjdapi()
        jd.connect(self.email, self.password)
        print('INFO: ' + 'Connected!')
        print('INFO: ' + 'Sending URL to JDownloader...')
        jd.get_device(device_id=self.device_id).linkgrabber.add_links([{"autostart": True, "links": self.l, "packageName": "TEST"}])
        print('INFO: ' + 'Your link was sent to JDownloader successfully!')
