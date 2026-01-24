import typer
import psutil
from datetime import datetime

def show_user():
    users = psutil.users()
    typer.echo()
    typer.echo(typer.style("=== USERS INFORMATION: ===", fg=typer.colors.YELLOW, bold=True))
    typer.echo(typer.style(f"Login users: {len(users)}", fg=typer.colors.GREEN, bold=True))

    if not users:
        typer.echo(typer.style(f"No active user", fg=typer.colors.GREEN, bold=True))
        return
    
    typer.echo()
    typer.echo(typer.style(
        f"{'USER':<15} {'TTY':<10} {'HOST':<20} {'LOGIN TIME'}",
        fg=typer.colors.CYAN, bold=True
    ))

    for u in users:
        login_time = datetime.fromtimestamp(u.started).strftime("%d %H:%M:%S")
        typer.echo(
            f"{u.name:<15} "
            f"{(u.terminal or '-'):<10} "
            f"{(u.host or '-'):<20} "
            f"{login_time}"
        )