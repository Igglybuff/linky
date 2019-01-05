import requests
import bs4


class Fmovies:

    def __init__(self, config):
        self.config = config
        pass

    def search_query(self, search_query):
        print('INFO: Searching FMovies for "' + search_query + '"...')
        return '<URL>'
