import typer



from .show_user import show_user

def commands_users_update(app: typer.Typer):

    @app.command("users", help="Show all user")
    def user_show():
        show_user()
        raise typer.Exit()
