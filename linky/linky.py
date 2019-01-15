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
    pusher = LinkPusher(config, ctx.obj['SILENCE'])
    pusher.push_links(links, download_client)


@linky.command()
@click.option('-i', '--indexer', 'indexers', envvar='LINKY_INDEXERS',
              required=False, default=None, help='One or more indexers to search.')
@click.option('-q', '--query', 'query', required=True, help='Search terms you would like to query, e.g. "Deadpool"')
@click.pass_context
def search(ctx, indexers, query):
    parser = ConfigParser(ctx.obj['CONFIG'], ctx.obj['SILENCE'])
    config = parser.get_config_dict()
    indexer = parser.get_indexers(indexers)
    searcher = IndexerSearcher(config, ctx.obj['SILENCE'])
    searcher.search(query, indexer)


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
