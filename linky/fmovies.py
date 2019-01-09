import requests
from bs4 import BeautifulSoup
from urllib3 import disable_warnings
# from selenium import webdriver


class Fmovies:

    disable_warnings()

    def __init__(self, config):
        self.config = config
        pass

    def search(self, query):
        print('INFO: Searching FMovies for "' + query + '"...')
        url = str(self.config['indexer fmovies']['url'])

        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

        params = (
            ('keyword', query),
        )

        page = requests.get(url + '/search', headers=headers, params=params)
        soup = BeautifulSoup(page.text, 'html.parser')
        html_results = soup.find_all('a', {"class": "name"})
        result_url = [result['href'] for result in html_results]
        top_result_page_url = url + result_url[0]

        # driver = webdriver.Chrome()
        # driver.get(top_result_page_url)
        # page = driver.page_source
        # print(page)
        # soup = BeautifulSoup(page, 'html.parser')
        # openload_url = soup.find_all()

        return '<URL>'

    def get_cookie(self, url):

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        }

        response = requests.get(url, headers=headers, verify=False)
        cookie = '; '.join([x.name + '=' + x.value for x in response.cookies])

        return cookie
