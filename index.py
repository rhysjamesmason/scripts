# Imports to the script
import os
from colorama import Fore, Back, Style
from sys import platform
from pick import pick
# from modules.ubuntu import UbuntuMainThread

# Ubuntu.py
active = True

# Sub functions


def UpdateManager():
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [Update Manager | Ubuntu]: "
        + Style.RESET_ALL
        + " Starting update process..."
    )

    # Telling the system to update the system/packages
    os.system("sudo apt update")
    os.system("sudo apt upgrade")

    # Completion message
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [Update Manager | Ubuntu]: "
        + Style.RESET_ALL
        + " Completed update process..."
    )
    print("\n")

    # Auto-update function
    def enableAutoUpdate():
        print(
            Fore.WHITE
            + Back.YELLOW
            + " INFO [Update Manager | Ubuntu]: "
            + Style.RESET_ALL
            + " Enabling the auto update."
        )
        os.system("sudo apt-get install auto-upgrades")
        os.system("sudo dpkg-reconfigure unattended-upgrades")
        pass

    # Ask if they want to enable auto update
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [Update Manager | Ubuntu]: "
        + Style.RESET_ALL
        + " Do you want to enable auto-update on this system? [yes (default) | no]"
    )
    answer = str(input("> "))

    # Checks if the user wants automatic updates
    if answer == "no" or answer == "n":
        return
    elif answer == "yes" or answer == "y" or answer == "":
        enableAutoUpdate()
        return
    else:
        print(
            Fore.WHITE
            + Back.RED
            + " ERROR [main | config]: "
            + Style.RESET_ALL
            + " Invalid input, Exiting... "
        )
        exit()


def UserManagementSystem():
    # While loop

    os.system("clear")
    # Option menu settings
    OPTION_TITLE = "What will you like to manage: "
    OPTION_OPTIONS = ["Check Users", "Check Groups", "Finished with UMS"]

    option, index = pick(OPTION_OPTIONS, OPTION_TITLE)

    if option == "Check Users":
        outputUsers = grp.getgrall()
        users = ["Back to Menu"]

        for group in outputUsers:
            for user in group[3]:
                users.append(user)

        print(type(group[0]))
        GROUP_OPTION_TITLE = "Select the user you want to manage:"
        option, index = pick(users, GROUP_OPTION_TITLE)
        pass
    elif option == "Check Groups":
        outputGroups = grp.getgrall()
        groups = ["Back to Menu"]

        for group in outputGroups:
            groups.append(group[0])

        print(type(group[0]))
        GROUP_OPTION_TITLE = "Select the group you want to manage:"
        option, index = pick(groups, GROUP_OPTION_TITLE)
        pass
    elif option == "Finished with UMS":
        global active
        active = False
        return


# Program Management

# SSH Server Install


def PMSSSH():
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | SSH | Ubuntu]: "
        + Style.RESET_ALL
        + " Installing 'Open SSH Server' and 'net-tools'."
    )
    os.system("sudo apt-get install openssh-server net-tools -y")
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | SSH | Ubuntu]: "
        + Style.RESET_ALL
        + " Opening SSH Port (22)."
    )
    os.system("sudo ufw allow ssh")
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | SSH | Ubuntu]: "
        + Style.RESET_ALL
        + " Enabling SSH Server on Boot."
    )
    os.system("sudo systemctl enable ssh")


# Webmin


def PMSWEBMIN():
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | WEBMIN | Ubuntu]: "
        + Style.RESET_ALL
        + " Installing 'software-properties-common, apt-transport-https'."
    )
    os.system("sudo apt install software-properties-common apt-transport-https -y")
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | WEBMIN | Ubuntu]: "
        + Style.RESET_ALL
        + " Enable Webmin Repository."
    )
    os.system(
        'sudo add-apt-repository "deb [arch=amd64] http://download.webmin.com/download/repository sarge contrib"'
    )
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | WEBMIN | Ubuntu]: "
        + Style.RESET_ALL
        + " Installing 'Webmin'."
    )
    os.system("sudo apt install webmin -y")
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | WEBMIN | Ubuntu]: "
        + Style.RESET_ALL
        + " Configuring the firewall."
    )
    os.system("sudo ufw allow 10000/tcp")
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | WEBMIN | Ubuntu]: "
        + Style.RESET_ALL
        + " Reloading the firewall."
    )
    os.system("sudo ufw reload")
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | WEBMIN | Ubuntu]: "
        + Style.RESET_ALL
        + " Enter a new root password for webmin."
    )
    passwrd = input(">")
    os.system(
        "sudo /usr/share/webmin/changepass.pl /etc/webmin root {0}".format(passwrd)
    )


# File Share with samba


def PMSSAMBA():
    pass


# Main Functions


def ProgramManageSystem():
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [PMS | Ubuntu]: "
        + Style.RESET_ALL
        + " What programs do you want to install?"
    )

    OPTION_TITLE = "Please select the program and hit enter to install:"
    OPTION_OPTIONS = [
        "SSH Server (requires manual config)",
        "Webmin (Remote Administator Management)",
        "Finished",
    ]

    option, index = pick(OPTION_OPTIONS, OPTION_TITLE)

    if option == "SSH Server (requires manual config)":
        PMSSSH()
    elif option == "Webmin (Remote Administator Management)":
        PMSWEBMIN()
    elif option == "Finished":
        global active
        active = False


# Main Functions


def UbuntuMainThread():
    print(
        Fore.WHITE
        + Back.CYAN
        + " INFO [main | config]: "
        + Style.RESET_ALL
        + Style.BRIGHT
        + " DISTRO => Ubuntu"
        + Style.RESET_ALL
    )
    print("\n")
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [main | Ubuntu]: "
        + Style.RESET_ALL
        + " Starting Update Manager..."
    )
    UpdateManager()
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [main | Ubuntu]: "
        + Style.RESET_ALL
        + " Finished with Update Manager..."
    )
    # print(Fore.WHITE + Back.YELLOW +
    #       " INFO [main | Ubuntu]: " + Style.RESET_ALL + " Starting User Management System (UMS)...")
    # while active:
    #     UserManagementSystem()

    # print(Fore.WHITE + Back.YELLOW +
    #     " INFO [main | Ubuntu]: " + Style.RESET_ALL + " Finished with User Management System (UMS)...")
    global active
    active = True
    print(
        Fore.WHITE
        + Back.YELLOW
        + " INFO [main | Ubuntu]: "
        + Style.RESET_ALL
        + " Starting Program Management System (PMS)..."
    )
    while active:
        ProgramManageSystem()
    pass


# Message to welcome user

# Clear the console
if platform == "linux" or platform == "linux2":
    os.system('clear')
    print("\n")
else:
    print(Fore.WHITE + Back.RED + " ERROR [main]: " + Style.RESET_ALL + " This script does not support Windows. ")
    exit(0)

print(Fore.WHITE + Back.BLUE + " INFO [main]: " + Style.RESET_ALL + " The script is initializing")

# Check for the Linux Distro.
print("\n")

print(Fore.WHITE + Back.CYAN + " INFO [main | config]: " + Style.RESET_ALL + " Please Select your distrobution below:")
print(Fore.WHITE + Back.CYAN + " OPTION [main | config]: " + Style.RESET_ALL + " [1] Ubuntu")
print(Fore.WHITE + Back.CYAN + " OPTION [main | config]: " + Style.RESET_ALL + " [2] Fedora")

def checkDistro():
    distro = str(input("\nPlease input the number [1 | 2]: "))
    return distro

# Option menu settings
OPTION_TITLE="Please select your distrobution of linux: "
OPTION_OPTIONS=["Ubuntu", "Fedora"]

option, index = pick(OPTION_OPTIONS, OPTION_TITLE)

# Check for the input
if option == "Ubuntu":
    print(Fore.WHITE + Back.CYAN + " INFO [main | config]: " + Style.RESET_ALL + Style.BRIGHT + " DISTRO => Ubuntu" + Style.RESET_ALL)
    os.system('clear')
    UbuntuMainThread()
elif option == "Fedora":
    print(Fore.WHITE + Back.CYAN + " INFO [main | config]: " + Style.RESET_ALL + Style.BRIGHT + " DISTRO => Fedora" + Style.RESET_ALL)


# Pause the script
input("Hit enter to exit...")
