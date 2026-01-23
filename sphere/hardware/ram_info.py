import typer
import psutil
import os
import struct


def to_gb(bytes: int):
    return f"{bytes / (1024 ** 3):.2f} GB"

def ram_show(mode: str):

    if mode == "minimal":
        minimal()
    elif mode == "full":
        full()
    else:
        typer.echo("Please specify a valid mode: '-m' or '-f'.")
    # ram = psutil.virtual_memory()
    # typer.echo()
    # typer.echo(typer.style("RAM Information:", fg=typer.colors.GREEN, bold=True))

    # typer.echo(f"Total:     {to_gb(ram.total)}")
    # typer.echo(f"Used:      {to_gb(ram.used)}")
    # typer.echo(f"Available: {to_gb(ram.available)}")
    # typer.echo(f"Free:      {to_gb(ram.free)}")
    # typer.echo(f"Usage:     {ram.percent}%")

def minimal():
    ram = psutil.virtual_memory()

    typer.echo()
    typer.echo(typer.style("Minimal RAM Information:", fg=typer.colors.GREEN, bold=True))

    typer.echo(f"Total:     {to_gb(ram.total)}")
    typer.echo(f"Used:      {to_gb(ram.used)}")
    typer.echo(f"Available: {to_gb(ram.available)}")
    typer.echo(f"Free:      {to_gb(ram.free)}")
    typer.echo(f"Usage:     {ram.percent}%")

def full():
    ram = psutil.virtual_memory()
    mmr_info = typeDDR()
    
    typer.echo()
    typer.echo(typer.style("Full RAM Information:", fg=typer.colors.GREEN, bold=True))
    typer.echo()

    typer.echo(f"Total:     {to_gb(ram.total)}")
    typer.echo(f"Used:      {to_gb(ram.used)}")
    typer.echo(f"Available: {to_gb(ram.available)}")
    typer.echo(f"Free:      {to_gb(ram.free)}")
    typer.echo(f"Usage:     {ram.percent}%")
    if isinstance(mmr_info, str):
        typer.echo()
        typer.echo(typer.style(f"Memory modules", fg=typer.colors.YELLOW, bold=True))
        typer.echo(f"{mmr_info}")
    else:
        installed = [mem for mem in mmr_info if mem['size_mb'] not in [0, 'Unknown']]
        empty_slots = len(mmr_info) - len(installed)
        
        typer.echo()
        typer.echo(typer.style("Memory Modules:", fg=typer.colors.GREEN, bold=True))
        typer.echo(f"  Total slots:       {len(mmr_info)}")
        typer.echo(f"  Installed modules: {typer.style(str(len(installed)), fg=typer.colors.GREEN, bold=True)}")
        typer.echo(f"  Empty slots:       {empty_slots}")
        
        if installed:
            typer.echo()
            typer.echo(typer.style("Installed Memory:", fg=typer.colors.CYAN, bold=True))
            typer.echo()
            
            typer.echo(f"  {'Module':<10} {'Type':<12} {'Size':<15} {'Slot':<10}")
            typer.echo(f"  {'-' * 10} {'-' * 12} {'-' * 15} {'-' * 10}")
            
            for i, mem in enumerate(installed, 1):
                size_gb = mem['size_mb'] / 1024
                module_num = f"Module {i}"
                mem_type = mem['type']
                size_str = f"{size_gb:.0f} GB ({mem['size_mb']} MB)"
                slot = mem['slot']
                
                typer.echo(
                    f"  {typer.style(module_num, fg=typer.colors.WHITE):<10} "
                    f"{typer.style(mem_type, fg=typer.colors.MAGENTA, bold=True):<12} "
                    f"{typer.style(size_str, fg=typer.colors.YELLOW):<15} "
                    f"{typer.style(slot, fg=typer.colors.CYAN):<10}"
                )
    
    typer.echo()
    typer.echo(typer.style("=" * 60, fg=typer.colors.CYAN))
    typer.echo()



## ===== Basic info =====

def typeDDR() ->  str:
    path = "/sys/firmware/dmi/entries"

    mmr_type = {
        0x12: "DDR",
        0X13: "DDR2",
        0X14: "DDR2 FB-DIMM",
        0X18: "DDR3",
        0X19: "FBD2",
        0X1A: "DDR4",
        0X1B: "LPDDR",
        0X1C: "LPDDR2",
        0X1D: "LPDDR3",
        0X1E: "LPDDR4",
        0X1F: "Logical non-volatile device",
        0x20: "HBM",
        0x21: "HBM2",
        0x22: "DDR5",
        0x23: "LPDDR5"
    }
    results = []

    for entry in os.listdir(path):
        if entry.startswith("17-"):
            raw_file = os.path.join(path, entry, "raw")

            try: 
                with open(raw_file, "rb") as f:
                    data = f.read()

                    if len(data) > 0x12:
                        mem_type_code = data[0x12]
                        mem_type = mmr_type.get(mem_type_code, f"Unknown (0x{mem_type_code:02X})")

                        if len(data) > 0x0D:
                            size = struct.unpack("<H", data[0x0C:0x0E])[0]
                            size_mb = size if size != 0xFFFF and size != 0x7FFF else "unknown"
                        else:
                            size_mb = "unknown"

                        results.append({
                            "slot": entry,
                            "type": mem_type,
                            "size_mb": size_mb 
                        })
            except PermissionError:
                return "root rights are required. Use sudo sph ram -f"
            except Exception as err:
                typer.echo(f"Error read {entry}")
    return results