import typer



from .net_show import net_show
from .handle_net_flags import handle_net_flags

def commands_net(app: typer.Typer):
    
    @app.command("net", help="Show NET information -m for minimal, -f for full")
    def net(   
        minimal: bool = typer.Option(False, "-m", help="Show minimal NET info"),
        full: bool = typer.Option(False, "-f", help="Show full NET info")
        ):
        mode = handle_net_flags(minimal, full)
        net_show(mode)
        raise typer.Exit() 