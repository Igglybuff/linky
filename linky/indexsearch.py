from sys import exit
from .fmovies import Fmovies
from .cinebloom import Cinebloom
from .orion import Orion
from .log import warning, info, error


class IndexerSearcher:

    def __init__(self, config, silence=False):
        self.config = config
        self.silence = silence

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
            error(False, 'Something went wrong searching for "' + query + '"')

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
