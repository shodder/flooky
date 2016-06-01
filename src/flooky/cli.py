
import click

@click.group()
def cli():
    pass


@cli.command()
@click.option('--host', default='localhost')
@click.option('--port', default=5000)
@click.option('--debug', is_flag=True)
def run(host, port, debug):
    from flooky.app import create_app
    from flooky import config

    app = create_app(config=config.DevelopmentConfig)
    app.run(host=host, port=port, debug=debug)

