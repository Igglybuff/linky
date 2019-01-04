import click


@click.command()
@click.option('-l', '--link', 'links', required=True, help='The URL to a file on a premium host that you want to download.')
@click.option('-c', '--config', 'config', envvar='LINKY_CONFIG_PATH', required=True, default='~/.config/linky/linky.conf', show_default=True, help='The path to your Linky configuration file.')
@click.option('-d', '--downloader', 'downloader', envvar='LINKY_DOWNLOADER', default='not_specified', help='The name of the download manager you want to use from your configuration file.')
def linky(links, config, downloader):
    """
    config = ConfigParser(config)
    config_dict = config.get_config_dict()
    """

