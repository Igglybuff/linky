import click
from os.path import expanduser
from .linkpush import LinkPusher
from .config import ConfigParser
from .indexsearch import IndexerSearcher


@click.group()
@click.option('-c', '--config', 'config',
              envvar='LINKY_CONFIG_PATH', required=True,
              default=expanduser("~") + '/.config/linky/linky.conf',
              show_default=True, help='The path to your Linky configuration file.')
@click.pass_context
def linky(ctx, config):
    ctx.obj = {
        'CONFIG': config,
    }


@linky.command()
@click.option('-l', '--link', 'links', required=True,
              help='The URL to a file on a premium host that you want to download.')
@click.option('-d', '--downloader', 'downloader', envvar='LINKY_DOWNLOADER', default=None,
              help='The name of the download manager you want to use from your configuration file.')
@click.pass_context
def push(ctx, links, downloader):
    parser = ConfigParser(ctx.obj['CONFIG'])
    config = parser.get_config_dict()
    download_client = parser.get_client(downloader)
    pusher = LinkPusher(config)
    pusher.push_links(links, download_client)


@linky.command()
@click.option('-i', '--indexer/--indexers', 'indexers', envvar='LINKY_INDEXERS',
              required=False, default=None, help='One or more indexers to search.')
@click.option('-q', '--query', 'query', required=True, help='Search terms you would like to query, e.g. "Deadpool"')
@click.pass_context
def search(ctx, indexers, query):
    parser = ConfigParser(ctx.obj['CONFIG'])
    config = parser.get_config_dict()
    indexer = parser.get_indexers(indexers)
    searcher = IndexerSearcher(config)
    searcher.search(query, indexer)
