import typer

from typing import List, Optional
from pathlib import Path

from sphere import app_version

import  sphere_native_rust

from .hardware.net_show import net_show

from .hardware.net_show import net_show, handle_net_flags
from .hardware.ram_info import ram_info, handle_ram_flags
from .hardware.cpu_info import cpu_info, handle_cpu_flags
from .hardware.users import show_user
from .install import install_main

from . import logo
from .hardware import disk
from enum import Enum


app = typer.Typer(help="Sphere {version} Command Line Interface".format(version=app_version.VERSION))

@app.command("install", help=" ")
def install(package: str):

    install_main.install(package)

    raise typer.Exit()


@app.command("v", help="Show application version")
def v():
    typer.echo(app_version.VERSION)
    raise typer.Exit()

@app.command("logo", help="Show application logo")
def logo_show():
    logo.show_logo()
    typer.echo(typer.style(f"You use: {app_version.VERSION} version", fg=typer.colors.YELLOW))
    raise typer.Exit()


@app.command("users", help="Show all user")
def user_show():
    show_user.show_user()
    raise typer.Exit()


@app.command("cpu", help="Show CPU information -m for minimal, -f for full")
def cpu(   
    minimal: bool = typer.Option(False, "-m", help="Show minimal CPU info"),
    full: bool = typer.Option(False, "-f", help="Show full CPU info")
    ):
    mode = handle_cpu_flags.handle_cpu_flags(minimal, full)
    cpu_info.cpu_show(mode)
    raise typer.Exit() 


@app.command("net", help="Show NET information -m for minimal, -f for full")
def net(   
    minimal: bool = typer.Option(False, "-m", help="Show minimal NET info"),
    full: bool = typer.Option(False, "-f", help="Show full NET info")
    ):
    mode = handle_net_flags.handle_net_flags(minimal, full)
    net_show.net_show(mode)
    raise typer.Exit() 

@app.command("ram", help="Show RAM information -m for minimal, -f for full")
def ram(
    minimal: bool = typer.Option(False, "-m", help="Show minimal RAM info"),
    full: bool = typer.Option(False, "-f", help="Show full RAM info")
    ):
    mode = handle_ram_flags.handle_ram_flags(minimal, full)
    ram_info.ram_show(mode)
    raise typer.Exit()


if __name__ == "__main__":
    app()