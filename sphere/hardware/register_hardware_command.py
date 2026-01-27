
from .users.commands_users import commands_users
from .sph_show.commands_show import commands_sphfetch
from .ram_info.commands_ram import commands_ram
from .net_show.commands_net import commands_net
from .gpu_info.commands_gpu import commands_gpu
def register_hardware_commands(app):
    commands_users(app)
    commands_sphfetch(app)
    commands_ram(app)
    commands_net(app)
    commands_gpu(app)