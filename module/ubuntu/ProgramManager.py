from config.globals import bcolors, active

from app.ubuntu.ssh import PMSSSH
from app.ubuntu.webmin import PMSWEBMIN

def ProgramManageSystem():
    updatePre = bcolors.BOLD + bcolors.OKBLUE + '[PMS]:' + bcolors.ENDC

    print(f"{updatePre} What programs do you want to install?")

    OPTION_TITLE = "Please select the program and hit enter to install:"
    OPTION_OPTIONS = [
        bcolors.BOLD + "SSH Server (requires manual config)" + bcolors.ENDC,
        bcolors.BOLD + "Webmin (Remote Administator Management)" + bcolors.ENDC,
        bcolors.BOLD + "Finished" + bcolors.ENDC,
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
