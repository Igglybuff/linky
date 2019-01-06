from sys import exit
from .fmovies import Fmovies


class IndexerSearcher:

    def __init__(self, config):
        self.config = config

    def search(self, query, indexers):
        if indexers.lower() == 'fmovies':
            self.search_fmovies(query)
        else:
            print('ERROR: Something went wrong searching for "' + query + '"')
            exit(1)

    def search_fmovies(self, query):
        fm = Fmovies(self.config)
        url = fm.search(query)
        print(url)
