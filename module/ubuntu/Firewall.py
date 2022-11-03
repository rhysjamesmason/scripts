import os
from config.globals import bcolors, active

def FireWall():
    updatePre = bcolors.BOLD + bcolors.OKBLUE + '[Firewall]:' + bcolors.ENDC

    # Enabling Firewall
    os.system("sudo ufw enable")

    # Installing Fail2Ban
    print(f"{updatePre} Installing Fail2Ban...")
    os.system('sudo apt install fail2ban')