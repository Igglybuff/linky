import click

@click.command()
@click.option('-l', '--link', 'url', required=True)
@click.option('-c', '--config', 'config', envvar='LINKY_CONFIG_PATH', required=True, default='~/.config/linky/linky.conf', show_default=True, help='The path to your Linky configuration file.')
def linky(url, config):
    pass