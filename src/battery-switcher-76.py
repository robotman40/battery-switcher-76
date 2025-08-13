import configparser
import os
import sys
from lib import bs76_lib

# Function for files and directories in the program's directory
if __name__ == "__main__":
    """
    During the installation process, we need to run this program once to generate the configuration
    file and to avoid printing unneeded data at the moment, we will check for a flag from the install script
    """

    # Install type
    install_type = bs76_lib.get_install_type(os.path.dirname(sys.executable))

    # Command line items
    commands = sys.argv

    if len(commands) > 1 and commands[1] == "--first-run":
        sys.exit(0)

    # Config file
    config = configparser.ConfigParser()
    if install_type == bs76_lib.install_type.local:
        config.read("/usr/local/etc/battery-switcher-76/config.ini")
    elif install_type == bs76_lib.install_type.package:
        config.read("/etc/battery-switcher-76/config.ini")

    # Version information
    version = configparser.ConfigParser()
    if install_type == bs76_lib.install_type.local:
        version.read("/usr/local/etc/battery-switcher-76/version.ini")
    elif install_type == bs76_lib.install_type.package:
        version.read("/etc/battery-switcher-76/version.ini")
    
    if len(commands) == 1:
        print(f"Power profiles:\nOn Battery Power: {config['Config']['OnBattery']}\nCharging: {config['Config']['Charging']}")
    else:
        if commands[1] in ["onbattery", "charging"]:
            if len(commands) > 2:
                if commands[2] in ["battery", "balanced", "performance"]:
                    if os.getuid() == 0:
                        config["Config"][commands[1]] = commands[2]
                        with open("/usr/local/etc/battery-switcher-76/config.ini", 'w') as configfile:
                            config.write(configfile)

                        # Manually change the power profile state
                        if (bs76_lib.get_power_state() == bs76_lib.power_state.charging and commands[1] == "charging") or (bs76_lib.get_power_state() == bs76_lib.power_state.onbattery and commands[1] == "onbattery"):
                            bs76_lib.change_power_profile(commands[2])
                    else:
                        print("Root privileges is required to change the configuration")
                else:
                    print("An invalid power profile was inputted.")
            else:
                print(config["Config"][commands[1]])
        elif commands[1] in ["disable", "enable"]:
            if os.getuid() == 0:
                bs76_lib.change_service_state(commands[1])
            else:
                print("Enabling/disabling battery-switcher-76 requires root privileges.")
        elif commands[1] == "version":
            print(f"{version["Version"]["Major"]}.{version["Version"]["Minor"]}.{version["Version"]["Patch"]}")
        elif commands[1] == "help":
            print("To change your system's battery profile, follow the command format below:\n\nsudo battery-switcher-76 [power state] [profile]\n\nValid options for [power state] are \"onbattery\" and \"charging\".\n\nValid options for [profile] are \"battery\", \"balanced\", and \"performance\".\n\n")
            print("To simply get the configured power profile for a certain battery state, follow the command format below:\n\nbattery-switcher-76 [power state]\n\nValid options for [power state] are \"onbattery\" and \"charging\".\n\n")
            print("To disable or enable the program, follow the command format below:\n\nsudo battery-switcher-76 [disable/enable].")
        else:
            print("An invalid option was inputted. Type \"battery-switcher-76 help\" for a brief guide.")