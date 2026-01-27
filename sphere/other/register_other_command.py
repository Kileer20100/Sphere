
from .version.commands_version import commands_version
from .logo.commands_logo import commands_logo
def register_other_commands(app):
    commands_version(app)
    commands_logo(app)