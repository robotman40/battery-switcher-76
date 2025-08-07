import time
import configparser
import os
from lib import bs76_lib
import sys

if __name__ == "__main__":
    # Install type
    install_type = bs76_lib.get_install_type(os.path.dirname(sys.executable))

    # Get the path for future reference
    if install_type == bs76_lib.install_type.local:
        config_path = "/usr/local/etc/battery-switcher-76/config.ini"
    elif install_type == bs76_lib.install_type.package:
        config_path = "/etc/battery-switcher-76/config.ini"

    # Initialize previous charging state
    prev_charging_state = None

    # Get file modification time
    last_modified_config = os.path.getmtime(config_path)

    while True:
        charging_state = bs76_lib.get_power_state()

        # Read the configuration file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Only change profile if charging state changed
        if charging_state != prev_charging_state:
            # Always update the power profile if charging state changes
            if charging_state == bs76_lib.power_state.charging:
                bs76_lib.change_power_profile(config['Config']['Charging'])
            elif charging_state == bs76_lib.power_state.onbattery:
                bs76_lib.change_power_profile(config['Config']['OnBattery'])

            prev_charging_state = charging_state

        time.sleep(3) # Three second delay before next check to prevent high CPU usage