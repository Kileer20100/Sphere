
from .update.commands_update import commands_update
from .install.commands_install import commands_install
from .check_update.commands_check_update import commands_check_update

def register_pkg_commands(app):
    commands_update(app)
    commands_install(app)
    commands_check_update(app)