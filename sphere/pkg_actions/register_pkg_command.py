
from .update.commands_update import commands_update



def register_pkg_commands(app):
    commands_update(app)