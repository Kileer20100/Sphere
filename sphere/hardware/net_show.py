import typer
import psutil
import socket

def net_show(mode: str):

    if mode == "minimal":
        minimal()
    elif mode == "full":
        full()
    else:
        typer.echo("Please specify a valid mode: '-m' or '-f'.")


def minimal():
    typer.echo()
    typer.echo(typer.style("Minimal Net Information:", fg=typer.colors.GREEN, bold=True))
    typer.echo(typer.style("=== Network Interfaces ===", fg=typer.colors.CYAN, bold=True))
    print_interfaces()
    typer.echo()

def full():
    typer.echo()
    typer.echo(typer.style("Full Net Information:", fg=typer.colors.GREEN, bold=True))

    typer.echo(typer.style("=== Network Interfaces ===", fg=typer.colors.CYAN, bold=True))
    print_interfaces()
    
    typer.echo()
    typer.echo(typer.style("=== Active Connections ===", fg=typer.colors.CYAN, bold=True))
    print_connections()



def print_interfaces():
    for iface, addrs in psutil.net_if_addrs().items():
        typer.echo(typer.style(f"Interface: {iface}", fg=typer.colors.YELLOW))
        for addr in addrs:
            family_map = {socket.AF_INET: "IPv4", socket.AF_INET6: "IPv6"}
            family = family_map.get(addr.family, "Other")
            typer.echo(f"  {family:<6} | IP: {addr.address:<25} | Mask: {addr.netmask}")

def print_connections():
    typer.echo(f"{'Proto':<6} {'Local Address':<25} {'Remote Address':<25} {'Status'}")
    typer.echo("-" * 70)

    all_conn = psutil.net_connections(kind="inet")
    for conn in all_conn[:5]:
        proto_map = {socket.SOCK_STREAM: "TCP", socket.SOCK_DGRAM: "UDP"}
        proto = proto_map.get(conn.type, str(conn.type))
        
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "*"
        status = conn.status if conn.status else "---"

        status_color = typer.colors.GREEN if status == "ESTABLISHED" else typer.colors.WHITE
        
        line = f"{proto:<6} {laddr:<25} {raddr:<25} {typer.style(status, fg=status_color)}"
        typer.echo(line)

