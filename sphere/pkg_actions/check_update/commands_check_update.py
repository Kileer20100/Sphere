import typer



from .check_update import check_update

def commands_check_update(app: typer.Typer):
    
    @app.command(
        "check-update",
        help=(
            "Check for available system package updates.\n"
            "Supports multiple package managers (dnf, apt, pacman, zypper).\n"
            "Displays a list of packages that can be updated without actually performing the update.\n"
        )
    )
    def update_check():
        check_update()
        raise typer.Exit()