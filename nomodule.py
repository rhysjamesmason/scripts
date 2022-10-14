# Imports to the script
import os
from sys import platform
# from modules.ubuntu import UbuntuMainThread

# Ubuntu.py
active = True

# Sub functions


def UpdateManager():
    print(
        " INFO [Update Manager | Ubuntu]: "
        + " Starting update process..."
    )

    # Telling the system to update the system/packages
    os.system("sudo apt update")
    os.system("sudo apt upgrade")

    # Completion message
    print(
        " INFO [Update Manager | Ubuntu]: "
        + " Completed update process..."
    )
    print("\n")

    # Auto-update function
    def enableAutoUpdate():
        print(
            " INFO [Update Manager | Ubuntu]: "
            + " Enabling the auto update."
        )
        os.system("sudo apt-get install auto-upgrades")
        os.system("sudo dpkg-reconfigure unattended-upgrades")
        pass

    # Ask if they want to enable auto update
    print(
        " INFO [Update Manager | Ubuntu]: "
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
            " ERROR [main | config]: "
            + " Invalid input, Exiting... "
        )
        exit()


def UserManagementSystem():
    # While loop

    os.system("clear")
    # Option menu settings
    OPTION_TITLE = "What will you like to view: "
    OPTION_OPTIONS = ["Check Users", "Check Groups", "Finished with UMS"]

    # Print the options
    print("1" + OPTION_OPTIONS[0])
    print("2" + OPTION_OPTIONS[1])
    print("3" + OPTION_OPTIONS[2])
    
    option = str(input(OPTION_TITLE))

    if option == "1":
        outputUsers = grp.getgrall()
        users = ["Back to Menu"]

        for group in outputUsers:
            for user in group[3]:
                print(user)

        input('Hit enter to exit...')
        pass
    elif option == "2":
        outputGroups = grp.getgrall()
        groups = ["Back to Menu"]

        for group in outputGroups:
            print(group[0])
            
        input('Hit enter to exit...')
        pass
    elif option == "3":
        global active
        active = False
        return
    else:
      exit()

# Program Management

# SSH Server Install


def PMSSSH():
    print(
        " INFO [PMS | SSH | Ubuntu]: "
        + " Installing 'Open SSH Server' and 'net-tools'."
    )
    os.system("sudo apt-get install openssh-server net-tools -y")
    print(
        " INFO [PMS | SSH | Ubuntu]: "
        + " Opening SSH Port (22)."
    )
    os.system("sudo ufw allow ssh")
    print(
        " INFO [PMS | SSH | Ubuntu]: "
        + " Enabling SSH Server on Boot."
    )
    os.system("sudo systemctl enable ssh")


# Webmin


def PMSWEBMIN():
    print(
        " INFO [PMS | WEBMIN | Ubuntu]: "
        + " Installing 'software-properties-common, apt-transport-https'."
    )
    os.system("sudo apt install software-properties-common apt-transport-https -y")
    print(
        " INFO [PMS | WEBMIN | Ubuntu]: "
        + " Getting the debian file."
    )
    os.system(
        'wget https://netix.dl.sourceforge.net/project/webadmin/webmin/2.000/webmin_2.000_all.deb'
    )
    print(
        " INFO [PMS | WEBMIN | Ubuntu]: "
        + " Installing 'Webmin'."
    )
    os.system("sudo dpkg -i webmin_2.000_all.deb")
    print(
        " INFO [PMS | WEBMIN | Ubuntu]: "
        + " Configuring the firewall."
    )
    os.system("sudo ufw enable")
    os.system("sudo ufw allow 10000/tcp")
    print(
        " INFO [PMS | WEBMIN | Ubuntu]: "
        + " Reloading the firewall."
    )
    os.system("sudo ufw reload")
    print(
        " INFO [PMS | WEBMIN | Ubuntu]: "
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
        " INFO [PMS | Ubuntu]: "
        + " What programs do you want to install?"
    )

    OPTION_TITLE = "Please select the program and hit enter to install:"
    OPTION_OPTIONS = [
        "SSH Server (requires manual config)",
        "Webmin (Remote Administator Management)",
        "Finished",
    ]

    print("1" + OPTION_OPTIONS[0])
    print("2" + OPTION_OPTIONS[1])
    print("3" + OPTION_OPTIONS[2])
    
    option = str(input(OPTION_TITLE))

    if option == "1":
        PMSSSH()
    elif option == "2":
        PMSWEBMIN()
    elif option == "3":
        global active
        active = False


# Main Functions


def UbuntuMainThread():
    print(
        " INFO [main | config]: "
        + " DISTRO => Ubuntu"
    )
    print("\n")
    print(
        " INFO [main | Ubuntu]: "
        + " Starting Update Manager..."
    )
    UpdateManager()
    print(
        " INFO [main | Ubuntu]: "
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
        " INFO [main | Ubuntu]: "
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
    print(" ERROR [main]: " + " This script does not support Windows. ")
    exit(0)

print(" INFO [main]: " + " The script is initializing")

# Check for the Linux Distro.
print("\n")

print(" INFO [main | config]: " + " Please Select your distrobution below:")
print(" OPTION [main | config]: " + " [1] Ubuntu")
print(" OPTION [main | config]: " + " [2] Fedora")

def checkDistro():
    distro = str(input("\nPlease input the number [1 | 2]: "))
    return distro

# Option menu settings
OPTION_TITLE="Please select your distrobution of linux: "
OPTION_OPTIONS=["Ubuntu", "Fedora"]

print("1" + OPTION_OPTIONS[0])
print("2" + OPTION_OPTIONS[1])

option = str(input(OPTION_TITLE))

# Check for the input
if option == "1":
    print(" INFO [main | config]: " + " DISTRO => Ubuntu")
    os.system('clear')
    UbuntuMainThread()
elif option == "2":
    print(" INFO [main | config]: " + " DISTRO => Fedora")


# Pause the script
input("Hit enter to exit...")
