import click
from os.path import expanduser
from .linkpush import LinkPusher
from .config import ConfigParser
from .indexsearch import IndexerSearcher
from .statuscheck import StatusChecker


@click.group()
@click.option('-c', '--config', 'config',
              envvar='LINKY_CONFIG_PATH', required=True,
              default=expanduser("~") + '/.config/linky/linky.conf',
              show_default=True, help='The path to your Linky configuration file.')
@click.option('-s', '--silence', is_flag=True, default=False,
              help='Disable log/info output. NOTE: Error messages cannot be silenced.')
@click.pass_context
def linky(ctx, config, silence):
    ctx.obj = {
        'CONFIG': config,
        'SILENCE': silence,
    }


@linky.command()
@click.option('-l', '--link', 'links', required=True,
              help='The URL to a file on a premium host that you want to download.')
@click.option('-d', '--downloader', 'downloader', envvar='LINKY_DOWNLOADER', default=None,
              help='The name of the download manager you want to use from your configuration file.')
@click.pass_context
def push(ctx, links, downloader):
    parser = ConfigParser(ctx.obj['CONFIG'], ctx.obj['SILENCE'])
    config = parser.get_config_dict()
    download_client = parser.get_client(downloader)
    links = parser.split_list(links)
    pusher = LinkPusher(config, ctx.obj['SILENCE'])
    pusher.push_links(links, download_client)


@linky.command()
@click.option('-i', '--indexer', 'indexers', envvar='LINKY_INDEXERS',
              required=False, default=None, help='Comma-separated list of indexers to search.')
@click.option('-r', '--results', 'results', required=False, default=1,
              help='Number of results to return as a comma-separated list.')
@click.option('-h', '--hosters', 'hosters', required=False, default='openload',
              help='Comma-separated list of 1-click-hosters to query.')
@click.option('-t', '--query-type', 'query_type', required=False, default='keyword',
              help='Set a different query type instead of doing a keyword search (e.g. "imdb" to search by IMDB ID).')
@click.option('-m', '--media-type', 'media_type', default='movie', required=True,
              help='The type of media you want (i.e. "TV" or "Movie").')
@click.option('-q', '--quality', 'quality', required=False, default='hd1080',
              help='Desired video quality of links to return (e.g. "hd1080").')
@click.argument('query')
@click.pass_context
def search(ctx, indexers, query, results, hosters, query_type, media_type, quality):
    parser = ConfigParser(ctx.obj['CONFIG'], ctx.obj['SILENCE'])
    config = parser.get_config_dict()
    indexer = parser.get_indexers(indexers)
    searcher = IndexerSearcher(config, ctx.obj['SILENCE'])
    searcher.search(query, indexer, media_type, hosters, results, query_type, quality)


@linky.command()
@click.option('-d', '--downloader', 'downloader', envvar='LINKY_DOWNLOADER', default=None,
              help='The name of the download manager you want to use from your configuration file.')
@click.option('-l', '--links', 'links', envvar='LINKY_LINKS', default=None,
              help='URLs to files you have sent to your download manager.')
@click.option('-a', '--all', 'all_items', default=False,
              help='Get the status for all items in your download manager\' queue.')
@click.pass_context
def status(ctx, downloader, links, all_items):
    parser = ConfigParser(ctx.obj['CONFIG'], ctx.obj['SILENCE'])
    config = parser.get_config_dict()
    download_client = parser.get_client(downloader)
    status_checker = StatusChecker(config, download_client, ctx.obj['SILENCE'])
    status_checker.get_status(links, all_items)
