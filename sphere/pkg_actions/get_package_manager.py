import shutil

def get_package_manager():
    if shutil.which("dnf"):
        return "dnf"
    elif shutil.which("apt"):
        return "apt"
    elif shutil.which("pacman"):
        return "pacman"
    elif shutil.which("zypper"):
        return "zypper"
    else:
        return None


def info_pkg():
    pkg_mgr = get_package_manager()

    if pkg_mgr:
        print(f"Detected package manager: {pkg_mgr}")
    else:
        print("No supported package manager found.")