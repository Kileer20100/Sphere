import typer
import sys
from sphere.build.builder import build


from sphere import app_version


from .build.register_build_command import register_build_commands
from .register_all_commands import register_all_commands

app = typer.Typer(help="Sphere {version} Command Line Interface".format(version=app_version.VERSION))

register_all_commands(app)
register_build_commands(app)
# def main():
#     if len(sys.argv) < 3:
#         print("Usage: sph build linux-x-x-x")
#         return

#     if sys.argv[1] == "build":
#         build(sys.argv[2])


if __name__ == "__main__":
    app()