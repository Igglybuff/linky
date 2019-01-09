import requests
import json


class Orion:

    def __init__(self, config):
        self.config = config

    def get_query(self):
        """
            Figure out how to form API request by
            checking whether user does a keyword
            search or uses an ID.
        """
        pass

    def search(self, query, media_type):
        user_key = self.config['indexer orion']['user_key']
        app_key = self.config['indexer orion']['app_key']

        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

        params = (
            ('keyuser', user_key),
            ('keyapp', app_key),
            ('mode', 'stream'),
            ('action', 'retrieve'),
            ('type', media_type),
            ('idimdb', query),
            ('limitcount', 1),
            ('streamtype', 'hoster'),
            ('streamhoster', 'openload'),
            ('videoquality', 'hd1080'),
        )

        page = requests.get('https://api.orionoid.com', headers=headers, params=params)
        url = json.loads(page.text)['data']['streams'][0]['stream']['link']

        return url
