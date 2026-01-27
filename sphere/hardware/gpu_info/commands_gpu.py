import typer



from .gpu_info import gpu_show
from .handle_gpu_flags import handle_gpu_flags

def commands_gpu(app: typer.Typer):
    @app.command("gpu", help="Show GPU information -m for minimal, -f for full")
    def cpu(   
        minimal: bool = typer.Option(False, "-m", help="Show minimal GPU info"),
        full: bool = typer.Option(False, "-f", help="Show full GPU info")
        ):
        
        mode = handle_gpu_flags(minimal, full)
        gpu_show(mode)
        raise typer.Exit() 