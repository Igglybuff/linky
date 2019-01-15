import json
from .log import error, info, warning
import requests


class Pyload:

    def __init__(self, links, config, silence=False):
        self.l = links
        self.c = config
        self.silence = silence
        self.hostname = self.c['client pyload']['hostname']
        self.port = self.c['client pyload']['port']
        self.username = self.c['client pyload']['username']
        self.password = self.c['client pyload']['password']
        self.ssl = self.c['client pyload']['ssl']

        if self.ssl == 'true':
            protocol = 'https'
        else:
            protocol = 'http'

        self.url = protocol + '://' + self.hostname + ':' + self.port

    def check_config(self):
        pass

    def connect(self):
        info(self.silence, 'Connecting to PyLoad at ' + self.url)

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': self.url,
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': self.url + '/login',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7'
        }

        data = {
            'do': 'login',
            'username': self.username,
            'password': self.password
        }

        session = requests.session()
        session.post(self.url + '/login',  headers=headers, data=data)
        return session

    def send_to_pyload(self):
        session = self.connect()
        info(self.silence, 'Sending URL to pyLoad...')
        package_name = self.l.rsplit('/')

        headers = {
            'Content-Type': 'application/json',
        }

        resp = session.post(self.url + '/api/addPackage?name="' + package_name[-1] + '"&links=["' + self.l + '"]', headers=headers)
        if resp.ok:
            info(self.silence, 'Your link was sent to pyLoad successfully!')
        else:
            print('Response: ' + resp.text)
            error(self.silence, 'Something went wrong sending your link to pyLoad.')

    def check_link_status(self, link=None):
        session = self.connect()
        info(self.silence, 'Checking pyLoad queue...')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': self.url,
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/json',
        }

        resp = session.get(self.url + '/api/getQueue', headers=headers)
        json_resp = json.loads(resp.text)
        print(json.dumps(json_resp, indent=4, sort_keys=True))
