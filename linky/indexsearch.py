from sys import exit
from .fmovies import Fmovies
from .cinebloom import Cinebloom
from .orion import Orion


class IndexerSearcher:

    def __init__(self, config):
        self.config = config

    def search(self, query, indexers):
        # if indexers is a comma-separated list, turn it
        # into a list and search all of them
        if indexers.lower() == 'fmovies':
            self.search_fmovies(query)
        elif indexers.lower() == 'cinebloom':
            self.search_cinebloom(query)
        elif indexers.lower() == 'orion':
            self.search_orion(query)
        else:
            print('ERROR: Something went wrong searching for "' + query + '"')
            exit(1)

    def search_fmovies(self, query):
        fm = Fmovies(self.config)
        url = fm.search(query)
        print(url)

    def search_cinebloom(self, query):
        cb = Cinebloom(self.config)
        url = cb.search(query)
        print(url)

    def search_orion(self, query):
        orion = Orion(self.config)
        url = orion.search(query, 'movie')
        print(url)
