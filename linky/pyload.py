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

        resp = requests.post(self.url + '/login',  headers=headers, data=data)
        cookies = '; '.join([x.name + '=' + x.value for x in resp.cookies])
        return cookies

    def send_to_pyload(self):
        cookies = self.connect()
        info(self.silence, 'Sending URL to pyLoad...')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': self.url,
            'Upgrade-Insecure-Requests': '1',
            'Cookie': cookies,
            'Content-Type': 'application/json',
        }

        params = (
            ('name', self.l),
            ('links', self.l),
        )

        info(self.silence, 'Sending URL to pyLoad...')
        resp = requests.post(self.url + '/addPackage', headers=headers, params=params)

    def check_link_status(self):
        cookies = self.connect()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': self.url,
            'Upgrade-Insecure-Requests': '1',
            'Cookie': cookies,
            'Content-Type': 'application/json',
        }

        resp = requests.get(self.url + '/getQueue', headers=headers)
        print(json.dumps(resp, indent=4, sort_keys=True))
