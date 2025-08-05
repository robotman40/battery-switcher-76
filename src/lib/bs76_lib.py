import subprocess as sp
import os
from enum import Enum

# Shared classes
class install_type(Enum):
    local = 1
    package = 1

# Shared functions
def change_power_profile(profile):
    sp.run(["system76-power", "profile", profile])

def get_install_type(install_path):
    if install_path == "/usr/local/bin":
        return install_type.local
    elif install_path == "/usr/bin":
        return install_type.package