import typer



from .sph_show import sph_show

def commands_sphfetch(app: typer.Typer):
    
    @app.command("sphfetch", help="Display info about system and logo")
    def sphfetch():
        sph_show()
        raise typer.Exit()