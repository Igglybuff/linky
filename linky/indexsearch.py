from .fmovies import Fmovies
from .orion import Orion
from .log import warning, info, error


class IndexerSearcher:

    def __init__(self, config, silence=False):
        self.config = config
        self.silence = silence

    def search(self, query, indexers, media_type, hosters, results, query_type, quality):
        # TODO: if indexers is a comma-separated list, turn it
        # into a list and search all of them
        if query_type.lower() == 'imdb':
            search_id = 'idimdb'
        elif query_type.lower() == 'tvdb':
            search_id = 'idtvdb'
        elif query_type.lower() == 'tmdb':
            search_id = 'idtmdb'
        elif query_type.lower() == 'keyword':
            search_id = 'query'
        else:
            error(False, 'Invalid query type "{}" specified.'.format(query_type))

        if indexers.lower() == 'fmovies':
            self.search_fmovies(query)
        elif indexers.lower() == 'orion':
            self.search_orion(query, media_type, hosters, results, search_id, quality)
        else:
            error(False, 'Something went wrong searching for "' + query + '"')

    def search_fmovies(self, query):
        fm = Fmovies(self.config)
        url = fm.search(query)
        print(url)

    def search_orion(self, query, media_type, hosters, results, query_type, quality):
        orion = Orion(self.config)
        url = orion.search(query, media_type, hosters, results, query_type, quality)
        print(url)
