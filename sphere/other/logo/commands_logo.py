import typer



from .logo import show_logo
from ...app_version import VERSION

def commands_logo(app: typer.Typer):
    
    @app.command("logo", help="Show application logo")
    def logo_show():
        show_logo()
        typer.echo(typer.style(f"You use: {VERSION} version", fg=typer.colors.YELLOW))
        raise typer.Exit()