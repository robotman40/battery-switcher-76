# **DISCLAIMER: THIS PROJECT IS NOT AFFILIATED WITH System76 or Pop!_OS. IT IS MERELY A PASSION PROJECT DONE FOR THE SAKE OF UTILITY. ADDITIONALLY, WHILE I HAVE VERIFIED IT WORKS ON MY END WITHOUT BREAKING ANYTHING, I WILL NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGE AS THIS IS ALPHA-QUALITY SOFTWARE.**

# Battery-Switcher-76
An automatic battery profile switcher that is intended for use on Pop!_OS and other systems utilizing [system76-power]([url](https://github.com/pop-os/system76-power)).

# How does it work?
It is split into two components: battery-switcher-76 and battery-switcher-76-service. The former is a user-end cli program that manages the program's configuration and information. The latter is the magic behind the program: it changes the battery profile by running commands in system76-power when a change in power state is detected.

# How do I install this?
You must be using a working version of Python and install the following libraries via `pip`:
- PyInstaller
- psutil

Additionally, you must be running a Linux distro using `systemd`. And obviously, you will need to use `system76-power`.

Once you have downloaded the program's source code, run `./install` in the directory it is shipped in. It will ask for `sudo` privileges once it is done building the program in order to install the program in the relevant directories.

I plan to ship precompiled binaries at some point in .tar.gz and .deb formats, but please use the installation script in the interim.

# How do I use this program?
In the command line, typing `battery-switcher-76` will give you information about the current configuration. An example result is:
```
Power profiles:
On Battery Power: battery
Charging: performance
```
To get information about the configuration about a specific power profile, type `battery-switcher-76 [power state]` with the valid options for `[power state]` being `onbattery` and `charging`. For example, if you type `battery-switcher-76 charging`, you may get:
```
performance
```
But to change a power profile for a specific power state, you must run `sudo battery-switcher-76 [power state] [profile]` with the valid options for `[power state]` being the same as the options mentioned above and for `[profile]` being `battery`, `balanced`, and `performance`.

If you need help using the program, you can type `battery-switcher-76 help` to print information about the program's usage.

# Future
## Planned Improvements and Additions
- Code refactoring
- Precompiled binaries in .tar.gz and .deb formats
- Improve the installation script's behavior

## Potential Improvements and Additions
- Additional features
- Binaries for other distros

While I am working actively on the planned updates, I am not doing the same for the potential ones and it may or may not come. I am going to start university relatively soon, which may siphon my time away from working on this project.

## Credits
- taxmeifyoucan
