# Imports to the script
import os
from sys import platform
from module.ubuntu.UpdateManager import UpdateManager
from module.ubuntu.Firewall import FireWall

from app.ubuntu.ssh import PMSSSH
from app.ubuntu.webmin import PMSWEBMIN

from config.globals import bcolors

active = True
mainPre = bcolors.BOLD + bcolors.OKBLUE + '[MAIN]:' + bcolors.ENDC

def ProgramManageSystem():
    updatePre = bcolors.BOLD + bcolors.OKBLUE + '[PMS]:' + bcolors.ENDC

    print(f"{updatePre} What programs do you want to install?")

    OPTION_TITLE = "Please select the program and hit enter to install:"
    OPTION_OPTIONS = [
        bcolors.BOLD + "SSH Server (requires manual config)" + bcolors.ENDC,
        bcolors.BOLD + "Webmin (Remote Administator Management)" + bcolors.ENDC,
        bcolors.BOLD + "Finished" + bcolors.ENDC,
    ]

    if programSSH == False and programWebmin == False:
        print(bcolors.OKCYAN + " 1: " + bcolors.ENDC + OPTION_OPTIONS[0])
        print(bcolors.OKCYAN + " 2: " + bcolors.ENDC + OPTION_OPTIONS[1])
        print(bcolors.OKCYAN + " 3: " + bcolors.ENDC + OPTION_OPTIONS[2])
    elif programSSH == True and programWebmin == False:
        print(bcolors.OKGREEN + " ✔️ 1: " + bcolors.ENDC + OPTION_OPTIONS[0])
        print(bcolors.OKCYAN + " 2: " + bcolors.ENDC + OPTION_OPTIONS[1])
        print(bcolors.OKCYAN + " 3: " + bcolors.ENDC + OPTION_OPTIONS[2])
    elif programSSH == False and programWebmin == True:
        print(bcolors.OKCYAN + " 1: " + bcolors.ENDC + OPTION_OPTIONS[0])
        print(bcolors.OKGREEN + " ✔️ 2: " + bcolors.ENDC + OPTION_OPTIONS[1])
        print(bcolors.OKCYAN + " 3: " + bcolors.ENDC + OPTION_OPTIONS[2])
    else:
        print(bcolors.OKGREEN + " ✔️ 1: " + bcolors.ENDC + OPTION_OPTIONS[0])
        print(bcolors.OKGREEN + " ✔️ 2: " + bcolors.ENDC + OPTION_OPTIONS[1])
        print(bcolors.OKCYAN + " 3: " + bcolors.ENDC + OPTION_OPTIONS[2])
    
    option = str(input(OPTION_TITLE))

    if option == "1":
        PMSSSH()
        global programSSH
        programSSH = True
    elif option == "2":
        PMSWEBMIN()
        global programWebmin
        programWebmin = True
    elif option == "3":
        global active
        active = False


# Main Functions


def UbuntuMainThread():
    osPre = bcolors.WARNING + "Ubuntu: " + bcolors.ENDC

    # Update Manager
    print(f"{osPre} Starting Update Manager...")
    UpdateManager()
    print(f"{osPre} Finished with Update Manager...")

    # Firewall

    print(f"{osPre} Starting Firewall...")
    FireWall()


    # Program Manager

    global active
    active = True
    programSSH = False
    programWebmin = False

    print(f"{osPre} Starting Program Management System (PMS)...")
    while active:
        os.system('clear')
        ProgramManageSystem()
    pass


# Message to welcome user

# Clear the console
if platform == "linux" or platform == "linux2":
    os.system('clear')
    print("\n")
else:
    print(f"{bcolors.FAIL}ERROR:{bcolors.ENDC} This script does not support Windows. ")
    exit(0)

print(f"{mainPre} The script is initializing")

# Check for the Linux Distro.
print("\n")

print(f"{mainPre} Please Select your distrobution below:")

def checkDistro():
    distro = str(input("\nPlease input the number [1 | 2]: "))
    return distro

# Option menu settings
OPTION_TITLE="Please select your distrobution of linux: "
OPTION_OPTIONS=["Ubuntu", "Fedora"]

print(bcolors.OKCYAN + " 1: " + bcolors.ENDC + bcolors.BOLD + OPTION_OPTIONS[0] + bcolors.ENDC)
print(bcolors.OKCYAN + " 2: " + bcolors.ENDC + bcolors.BOLD + OPTION_OPTIONS[1] + bcolors.ENDC)

option = str(input(OPTION_TITLE))

# Check for the input
if option == "1":
    print(f"{mainPre} DISTRO => Ubuntu")
    os.system('clear')
    UbuntuMainThread()
elif option == "2":
    print(f"{mainPre} DISTRO => Fedora")


# Pause the script
input("Hit enter to exit...")
