import requests
import json


class Orion:

    def __init__(self, config):
        self.config = config

    def search(self, query, media_type, hosters, results, search_id, quality):
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
            ('type', media_type.lower()),
            (search_id, query),
            ('limitcount', results),
            ('streamtype', 'hoster'),
            ('streamhoster', hosters.lower()),
            ('videoquality', quality.lower()),
        )

        page = requests.get('https://api.orionoid.com', headers=headers, params=params)

        links = []
        for link in json.loads(page.text)['data']['streams']:
            links.append(link['stream']['link'])

        urls = ",".join(links)

        return urls
