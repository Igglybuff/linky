import click

@click.command()
@click.option('-l', '--link', 'url', required=True, help='The URL to a file on a premium host that you want to download.')
@click.option('-c', '--config', 'config', envvar='LINKY_CONFIG_PATH', required=True, default='~/.config/linky/linky.conf', show_default=True, help='The path to your Linky configuration file.')
def linky(url, config):
    pass