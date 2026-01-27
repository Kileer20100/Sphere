
from .version.commands_version import commands_version
def register_other_commands(app):
    commands_version(app)