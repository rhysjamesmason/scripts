import os
from config.globals import bcolors

def UpdateManager():
    updatePre = bcolors.BOLD + bcolors.OKBLUE + '[UM]:' + bcolors.ENDC

    print(f"{updatePre} Program starting")

    # Telling the system to update the system/packages
    os.system("sudo apt update && sudo apt upgrade")

    # Completion message
    print(f"{updatePre} Completed update process...")

    # Auto-update function
    def enableAutoUpdate():
        print(f"{updatePre} Enabling the auto update.")
        os.system("sudo apt-get install auto-upgrades && sudo dpkg-reconfigure unattended-upgrades")
        pass

    # Ask if they want to enable auto update
    print(f"{updatePre} Do you want to enable auto-update on this system? [yes (default) | no]")
    answer = str(input("> "))

    # Checks if the user wants automatic updates
    if answer == "no" or answer == "n":
        return
    elif answer == "yes" or answer == "y" or answer == "":
        enableAutoUpdate()
        return
    else:
        print(f"{bcolors.FAIL}ERROR:{bcolors.ENDC} Invalid input, Exiting... ")
        exit()