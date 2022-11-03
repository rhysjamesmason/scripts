import os
from config.globals import bcolors

def PMSSSH():
    updatePre = bcolors.BOLD + bcolors.OKBLUE + '[PMS | SSH]:' + bcolors.ENDC

    print(f"{updatePre} Installing 'Open SSH Server' and 'net-tools'.")
    os.system("sudo apt-get install openssh-server net-tools -y")

    # Firewall Configuration
    print(f"{updatePre} Opening SSH Port (22).")
    os.system("sudo ufw allow ssh")

    # Start Up application
    print(f"{updatePre} Enabling SSH Server on Boot.")
    os.system("sudo systemctl enable ssh")