import typer
from .builder import build

def register_build_commands(app: typer.Typer):

    @app.command("build-kernel", help="Build Sphere kernel")
    def build_kernel(target: str):
        try:
            build(target)
        except ValueError as e:
            raise typer.BadParameter(str(e))
