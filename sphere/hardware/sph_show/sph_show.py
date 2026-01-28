import typer
import psutil
import platform
import os
import sys
import getpass
import re
import time
import socket

from ...lib.cpu import brand
from ...lib.gpu import gpu_name, gpu_type
from ...app_version import VERSION

def sph_show():
    users = psutil.users()
    for u in users:
        username = f"{u.name}"

    sys_info = platform.uname()
    typer.echo()
    import subprocess

    shell_path = os.environ.get("SHELL", "/bin/sh")

    try:
        result = subprocess.run(
            [shell_path, "--version"], 
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        match = re.search(r"\d+\.\d+(\.\d+)?", output)
        version = match.group(0) if match else "unknown"
    except Exception:
        version = "unknown"

    logo =  r"""
                     :=+***++-:                          
                  -*%@@@@@@@@@@%+:                  
                -%@@@@@@@@@@@@@@@@#-   .::::.       
              .*@@@@@@@@@@@@@@@@@@@@#%@%%@@@@%*.                    OS
             .%@@@@@@@@@@@@@@@@@@@@@@%.  .-%@@@=                    MotherBoard
             #@@@@@@@@@@@@@@@@@@@@@@@@*    *@@%.                    CPU     
            =@@@@@@@@@@@@@@@@@@@@@@@@@@-  -@@#.                     GPU
            %@@@@@@@@@@@@@@@@@@@@@@@@@@=.*@@+                       Memory
           :@@@@@@@@@@@@@@@@@@@@@@@@@+-*@@*.                        SPH
           :@@@@@@@@@@@@@@@@@@@@@@#=-*@%+.                          Shell
         .+%@@@@@@@@@@@@@@@@@@@#+-+%@#=-                            Uptime
        =%#:#@@@@@@@@@@@@@@@#==+%@%+-=##                            Boot
      :#@+  -@@@@@@@@@@@#+==*%@%+-=#@@@:                            Distro
     -@@*    *@@@@@%*===*%@%#=-=#@@@@@+                             Kernel
     %@@#.    =====+#%@%*=-=*%@@@@@@@+                              CPU Cores/Thears
     %@@@@####%@@@%#+=-=*%@@@@@@@@@%=                               AVG
      -+*##**+=-:.=*#@@@@@@@@@@@@@+.                
                  .=#%@@@@@@@@%*-.                  
                      :--==-:.                      ⠀⠀⠀⠀⠀
            """
    
    username = getpass.getuser()
    hostname = platform.node()
    mb = socket.gethostname()

    info = [
    "OS Information:",
    "",
    f"{username}@{sys_info.node}",
    "============",
    f"{platform.system()} {hostname.capitalize()} {sys_info.machine}",
    f"{get_motherb()}",
    f"{brand()}",
    f"{gpu_name()} {gpu_type()}",
    f"{ram_info()}",
    f"{VERSION}",
    f"{version}",
    f"{get_uptime()}",
    f"{boot_menu()}",
    f"{distro_info()}",
    f"{kernel_info()}",
    f"{cpu_cores()}",
    f"{load_avg()}"
    ]

    logo_lines = logo.splitlines()
    width = max(len(line) for line in logo_lines)
    # padding = 4

    for i in range(max(len(logo_lines), len(info))):
        left = logo_lines[i] if i < len(logo_lines) else ""
        right = str(info[i]) if i < len(info) and info[i] is not None else ""
        typer.echo(f"\033[34m{left.ljust(width)}\033[0m" + " " + right)




def get_uptime():
    uptime_sec = time.time() - psutil.boot_time()
    days = int(uptime_sec // 86400)
    hours = int((uptime_sec % 86400) // 3600)
    minutes = int((uptime_sec % 3600) // 60)

    uptime = ""
    if days > 0:
        uptime += f"{days}D "
    if hours > 0 or days > 0:
        uptime += f"{hours}H "
    if minutes > 0 or hours > 0 or days >0:
        uptime += f"{minutes}M "
    return uptime


def get_motherb():
    with open("/sys/class/dmi/id/board_name", "r") as f:
        return f.read().strip()
    

def to_gb(bytes: int):
    return f"{bytes / (1024 ** 3):.2f} GB"

def ram_info():
    ram = psutil.virtual_memory()
    return f"{to_gb(ram.used)}/{to_gb(ram.total)}"

def kernel_info():
    return f"{platform.release()} ({platform.version().split()[0]})"


def distro_info():
    try:
        with open("/etc/os-release") as f:
            data = f.read()
        name = re.search(r'^NAME="?(.*)"?$', data, re.M)
        version = re.search(r'^VERSION="?(.*)"?$', data, re.M)
        return f"{name.group(1)} {version.group(1)}"
    except Exception:
        return "Unknown"

def boot_menu():
    return "Boot: UEFI" if os.path.exists("sys/firmware/efi") else "Boot: Legacy"


def cpu_cores():
    return f"Cores {psutil.cpu_count(logical=False)} | Theads {psutil.cpu_count(logical=True)}"

def load_avg():
    try:
        l1, l5, l15 = os.getloadavg()
        return f"{l1:.2f}, {l5:.2f}, {l15:.2f}"
    except OSError:
        return "Error"