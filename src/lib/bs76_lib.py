import subprocess as sp

def change_power_profile(profile):
    sp.run(["system76-power", "profile", profile])