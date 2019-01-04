import myjdapi


class Jdownloader:

    def __init__(self, links, config):
        self.l = links
        self.c = config

    def check_config(self):
        self.check_email_format()
        self.check_device_id_validity()
        self.check_password_exists()

    def check_email_format(self):
        pass

    def check_password_exists(self):
        pass

    def check_device_id_validity(self):
        pass

    def send_to_jdownloader(self):
        email = self.c['jdownloader']['email']
        password = self.c['jdownloader']['password']
        device_id = self.c['jdownloader']['device_id']
        jd = myjdapi.Myjdapi()
        jd.connect(email, password)
        jd.get_device(device_id=device_id).linkgrabber.add_links([{"autostart": True, "links": self.l, "packageName": "TEST"}])
