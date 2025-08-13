import subprocess as sp
import psutil
from enum import Enum

# Shared classes
class install_type(Enum):
    local = 1
    package = 2

class power_state(Enum):
    onbattery = 1
    charging = 2

# Shared functions
def change_power_profile(profile):
    sp.run(["system76-power", "profile", profile], stdout=sp.DEVNULL, stderr=sp.DEVNULL)

def get_install_type(install_path):
    if install_path == "/usr/local/bin":
        return install_type.local
    elif install_path == "/usr/bin":
        return install_type.package
    
def get_power_state():
    battery_state = psutil.sensors_battery()
    if battery_state:
        return power_state.charging
    else:
        return power_state.onbattery
    
def change_service_state(state):
    if state == "enable":
        sp.run(["sudo", "systemctl", "enable", "battery-switcher-76"], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    elif state == "disable":
        sp.run(["sudo", "systemctl", "disable", "battery-switcher-76"], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    else:
        raise Exception("An invalid service state option was given")