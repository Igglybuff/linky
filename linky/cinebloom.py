import requests
from bs4 import BeautifulSoup
from urllib3 import disable_warnings


class Cinebloom:

    disable_warnings()

    def __init__(self, config):
        self.config = config
        pass

    def search(self, query):
        print('INFO: Searching Cinebloom for "' + query + '"...')
        url = str(self.config['indexer fmovies']['url'])

        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

        params = (
            ('q', query),
        )

        page = requests.get(url + '/searching', headers=headers, params=params)
        soup = BeautifulSoup(page.text, 'html.parser')
        html_results = soup.find_all('a', {"class": "name"})
        result_url = [result['href'] for result in html_results]
        top_result_page_url = url + result_url[0]
