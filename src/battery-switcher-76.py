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

    if len(sys.argv) > 1 and sys.argv[1] == "--first-run":
        sys.exit(0)

    config = configparser.ConfigParser()
    config.read("/usr/local/etc/battery-switcher-76/config.ini")
    # Command line items
    commands = sys.argv
    
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
                        # Change power manually
                        bs76_lib.change_power_profile(commands[2])
                    else:
                        print("Root privileges is required to change the configuration")
                else:
                    print("An invalid power profile was inputted.")
            else:
                print(config["Config"][commands[1]])
        elif commands[1] == "help":
            print("To change your system's battery profile, follow the command format below:\n\nbattery-switcher-76 [power state] [profile]\n\nValid options for [power state] are \"onbattery\" and \"charging\"\n\nValid options for [profile] are \"battery\", \"balanced\", and \"performance\".")
        else:
            print("An invalid option was inputted. Type \"battery-switcher-76 help\" for a brief guide.")