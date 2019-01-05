import click
from .linkpush import LinkPusher
from .config import ConfigParser


@click.command()
@click.option('-l', '--link', 'links', required=True, help='The URL to a file on a premium host that you want to download.')
@click.option('-c', '--config', 'config', envvar='LINKY_CONFIG_PATH', required=True, default='~/.config/linky/linky.conf', show_default=True, help='The path to your Linky configuration file.')
@click.option('-d', '--downloader', 'downloader', envvar='LINKY_DOWNLOADER', default=None, help='The name of the download manager you want to use from your configuration file.')
def linky(links, config, downloader):
    parser = ConfigParser(config, downloader)
    config = parser.get_config_dict()
    downloader = parser.set_client()
    push = LinkPusher(links, config, downloader)
    push.push_link()

# $ linky --search "rick and morty s03e01" (--indexer/-i orion|--all-indexers/-a) --config linky.conf --downloader jdownloader (--print)
