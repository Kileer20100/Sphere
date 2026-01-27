import typer

from ...app_version import VERSION

def commands_version(app: typer.Typer):
    @app.command("v", help="Show application version")
    def v():
        typer.echo(VERSION)
        raise typer.Exit()