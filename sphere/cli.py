import typer

from typing import List, Optional
from pathlib import Path

from sphere import app_version

import  sphere_native_rust
from .hardware import cpu_info, ram, disk
from enum import Enum




app = typer.Typer(help="Sphere {version} Command Line Interface".format(version=app_version.VERSION))




@app.command("v", help="Show application version")
def v():
    typer.echo(app_version.VERSION)
    raise typer.Exit()

@app.command("cpu", help="Show CPU information -m for minimal, -f for full")
def cpu(   
    minimal: bool = typer.Option(False, "-m", help="Show minimal CPU info"),
    full: bool = typer.Option(False, "-f", help="Show full CPU info")
    ):
    mode = handle_cpu_flags(minimal, full)
    cpu_info.cpu_show(mode)
    raise typer.Exit() 


def handle_cpu_flags(minimal: bool, full: bool) -> str:
    if minimal and full:
        typer.echo("Please specify only one option: '-m' or '-f'.")
        return "invalid"
    if full:
        return "full"
    elif minimal:
        return "minimal"
    else:
        return "invalid"

if __name__ == "__main__":
    app()