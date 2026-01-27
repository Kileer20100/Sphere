import typer
import sys
from sphere.build.builder import build

from typing import List, Optional
from pathlib import Path

from sphere import app_version

import  sphere_native_rust

from .hardware.net_show import net_show
from .hardware.sph_show import sph_show
from .hardware.net_show import net_show, handle_net_flags
from .hardware.ram_info import ram_info, handle_ram_flags
from .hardware.cpu_info import cpu_info, handle_cpu_flags
from .hardware.gpu_info import gpu_info, handle_gpu_flags
from .hardware.disk_show import disk_info, handle_disk_flags

from .hardware.users import show_user

from .pkg_actions.install import install_main
from .pkg_actions.update import update_main
from .pkg_actions.check_update import check_update


from .other.logo import logo
from enum import Enum


from .register_all_commands import register_all_commands

app = typer.Typer(help="Sphere {version} Command Line Interface".format(version=app_version.VERSION))

register_all_commands(app)

def main():
    if len(sys.argv) < 3:
        print("Usage: sph build linux-x-x-x")
        return

    if sys.argv[1] == "build":
        build(sys.argv[2])


if __name__ == "__main__":
    app()