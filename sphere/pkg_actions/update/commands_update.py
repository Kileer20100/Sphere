import typer



from .update_main import update_main

def commands_update(app: typer.Typer):
    
    @app.command(
        "update",
        help=(
            "Update system packages.\n"
            "Flags:\n"
            "  -y  auto-confirm all prompts\n"
            "  -q  quiet mode (minimal output)"
        )
    )
    def update(
        yes: bool = typer.Option(False, "-y", help="Automatically confirm all prompts (non-interactive update)."),
        quiet: bool = typer.Option(False, "-q", help="Reduce output verbosity. Show only important messages."),
    ):
        update_main(yes,quiet)
        raise typer.Exit()