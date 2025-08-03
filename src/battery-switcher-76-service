import psutil
import time
import configparser
from lib import bs76_lib

if __name__ == "__main__":
    # Initialize previous charging state
    prev_charging_state = None

    while True:
        config = configparser.ConfigParser()
        config.read("/usr/local/etc/battery-switcher-76/config.ini")
        
        battery = psutil.sensors_battery()
        charging_state = battery.power_plugged

        # Only change profile if charging state changed
        if charging_state != prev_charging_state:
            if charging_state:
                bs76_lib.change_power_profile(config['Config']['Charging'])
            else:
                bs76_lib.change_power_profile(config['Config']['OnBattery'])
            prev_charging_state = charging_state

        time.sleep(3) # Three second delay before next check to prevent high CPU usage