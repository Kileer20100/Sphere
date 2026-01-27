
from .pkg_actions.register_pkg_command import register_pkg_commands
from .hardware.register_hardware_command import register_hardware_commands
from .build.register_build_command import register_build_commands


def register_all_commands(app):

    register_pkg_commands(app)

    register_hardware_commands(app)
    
    register_build_commands(app)