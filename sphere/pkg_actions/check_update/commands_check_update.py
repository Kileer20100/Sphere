import typer



from .check_update import check_update

def commands_install(app: typer.Typer):
    
    @app.command("install", help="Install packages ")
    def install(package: str):
        install(package)
        raise typer.Exit()