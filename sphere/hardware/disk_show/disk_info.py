import typer
import psutil

def disk_show(mode: str):
    if mode == "minimal":
        minimal()
    elif mode == "full":
        full()
    else:
        typer.echo("Please specify a valid mode: '-m' or '-f'.")



def minimal():
    typer.echo()
    typer.echo(typer.style("=== MINIMAL DISK INFORMATION ===", fg=typer.colors.GREEN, bold=True))
    typer.echo()
    get_info_min()

def full():
    typer.echo()
    typer.echo(typer.style("=== FULL DISK INFORMATION ===", fg=typer.colors.GREEN, bold=True))
    typer.echo()

    get_info_full()



def to_gb(bytes: int):
    return f"{bytes / (1024 ** 3):.2f} GB"

def cut(text: str, width: int) -> str:
    return text[:width-1] + "…" if len(text) >= width else text


def get_info_full():
    partitions = psutil.disk_partitions()

    typer.echo(
        f"{'DEVICE':<14} {'MOUNT':<25} {'FS':<10} "
        f"{'TOTAL':>10} {'USED':>10} {'FREE':>10} {'USE%':>6}"
    )
    typer.echo("-" * 90)

    for p in partitions:
        try:
            u = psutil.disk_usage(p.mountpoint)
        except PermissionError:
            typer.echo(
                f"{cut(p.device,14):<14} {cut(p.mountpoint,25):<25} {cut(p.fstype,10):<10} "
                f"{'NO ACCESS':>10} {'-':>10} {'-':>10} {'-':>6}"
            )
            continue

        typer.echo(
            f"{cut(p.device,14):<14} "
            f"{cut(p.mountpoint,25):<25} "
            f"{cut(p.fstype,10):<10} "
            f"{to_gb(u.total):>10} "
            f"{to_gb(u.used):>10} "
            f"{to_gb(u.free):>10} "
            f"{str(u.percent) + '%':>6}"
        )

    disk_io = psutil.disk_io_counters()
    typer.echo()
    typer.echo(typer.style(f"Total read:  {to_gb(disk_io.read_bytes)}", fg=typer.colors.CYAN))
    typer.echo(typer.style(f"Total write: {to_gb(disk_io.write_bytes)}", fg=typer.colors.CYAN))

def get_info_min():
    partitions = psutil.disk_partitions()
    disk_io = psutil.disk_io_counters()

    typer.echo(typer.style(
        f"Total read: {to_gb(disk_io.read_bytes)} | Total write: {to_gb(disk_io.write_bytes)}",
        fg=typer.colors.CYAN
    ))

    typer.echo(
        f"{'DEVICE':<15} {'TOTAL':>10} {'USED':>10} {'FREE':>10} {'USE%':>6}"
    )
    typer.echo("-" * 55)

    for p in partitions:
        try:
            u = psutil.disk_usage(p.mountpoint)
        except PermissionError:
            typer.echo(typer.style("Root rights are required. Use sudo sph disk -f", fg=typer.colors.RED))
            continue

        typer.echo(
            f"{p.device:<15} "
            f"{to_gb(u.total):>10} "
            f"{to_gb(u.used):>10} "
            f"{to_gb(u.free):>10} "
            f"{str(u.percent) + '%':>6}"
        )
