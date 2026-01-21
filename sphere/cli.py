import typer

from typing import List, Optional
from pathlib import Path

from sphere import app_version

import  sphere_native_rust

app = typer.Typer(help="Sphere {version} Command Line Interface".format(version=app_version.VERSION))

@app.command()
def main(show_version: bool = typer.Option(False, '-v', '--version', help="Show application version"),
         show_cpu: bool = typer.Option(False, '-cpui', '--cpu_info', help="Show cpu version")):
    if show_version:
        typer.echo(app_version.VERSION)
        raise typer.Exit()
    if show_cpu:
        cpu_count = sphere_native_rust.cpu_count()
        typer.echo(f"CPU Count: {cpu_count}")
        raise typer.Exit()


if __name__ == "__main__":
    app()