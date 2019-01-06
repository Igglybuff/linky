import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


class Fmovies:

    def __init__(self, config):
        self.config = config
        pass

    def search(self, query):
        print('INFO: Searching FMovies for "' + query + '"...')
        url = str(self.config['indexer fmovies']['url'])
        cookie = self.get_cookie(url)
        search_url = url + '/search?keyword=' + quote_plus(query)

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7',
        }

        # page = requests.get('https://www.dvdsreleasedates.com/', headers=headers)
        # soup = BeautifulSoup(page.text, 'html.parser')
        # requested_table = soup.find("div", {"id": 'requested'})
        # requested_hrefs = requested_table.find_all('a')
        # movie_names = [movie.contents[0].replace(' ', '?') + "*," for movie in requested_hrefs]
        #
        # return movie_names
        return '<URL>'

    def get_cookie(self, url):

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        }

        response = requests.get(url, headers=headers, verify=False)
        cookie = '; '.join([x.name + '=' + x.value for x in response.cookies])

        return cookie
