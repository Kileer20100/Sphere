import typer

from typing import List, Optional
from pathlib import Path

from sphere import app_version

import  sphere_native_rust
from .hardware import cpu_info, ram_info, disk, logo, net_show
from enum import Enum


app = typer.Typer(help="Sphere {version} Command Line Interface".format(version=app_version.VERSION))




@app.command("v", help="Show application version")
def v():
    typer.echo(app_version.VERSION)
    raise typer.Exit()

@app.command("logo", help="Show application logo")
def logo_show():
    logo.show_logo()
    typer.echo(typer.style(f"You use: {app_version.VERSION} version", fg=typer.colors.YELLOW))
    raise typer.Exit()

@app.command("cpu", help="Show CPU information -m for minimal, -f for full")
def cpu(   
    minimal: bool = typer.Option(False, "-m", help="Show minimal CPU info"),
    full: bool = typer.Option(False, "-f", help="Show full CPU info")
    ):
    mode = handle_cpu_flags(minimal, full)
    cpu_info.cpu_show(mode)
    raise typer.Exit() 


@app.command("net", help="Show NET information -m for minimal, -f for full")
def net(   
    minimal: bool = typer.Option(False, "-m", help="Show minimal NET info"),
    full: bool = typer.Option(False, "-f", help="Show full NET info")
    ):
    mode = handle_cpu_flags(minimal, full)
    net_show.net_show(mode)
    raise typer.Exit() 

@app.command("ram", help="Show RAM information -m for minimal, -f for full")
def ram(
    minimal: bool = typer.Option(False, "-m", help="Show minimal RAM info"),
    full: bool = typer.Option(False, "-f", help="Show full RAM info")
    ):
    mode = handle_ram_flags(minimal, full)
    ram_info.ram_show(mode)
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

def handle_ram_flags(minimal: bool, full: bool) -> str:
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