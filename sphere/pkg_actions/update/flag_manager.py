from typing import Optional
import typer

UPDATE_FLAGS = {
    "dnf": {"-y": "-y", "-q": "-q", "-check": "check-update"},
    "apt": {"-y": "-y", "-q": "-q", "-check": "list --upgradable"},
    "pacman": {"-y": "--noconfirm", "-q": "-q", "-check": "-Qu"},
    "zypper": {"-y": "-y", "-q": "--quiet", "-check": "list-updates"}
}

def flag_update_manager(
        pkg: str,
        flag1: Optional[bool] = False,
        flag2: Optional[bool] = False
) -> list:

    flags = []
    manager_flags = UPDATE_FLAGS.get(pkg, {})

    if flag1 and "-y" in manager_flags:
        flags.append(manager_flags["-y"])

    if flag2 and "-q" in manager_flags:
        flags.append(manager_flags["-q"])

    

    return flags
