import os
from config.globals import bcolors

def PMSWEBMIN():
    updatePre = bcolors.BOLD + bcolors.OKBLUE + '[PMS | WEBMIN]:' + bcolors.ENDC

    print(f"{updatePre} Installing 'software-properties-common, apt-transport-https'.")
    os.system("sudo apt install software-properties-common apt-transport-https libauthen-pam-perl libio-pty-perl -y")

    print(f"{updatePre} Getting the debian file.")
    os.system(
        'wget https://netix.dl.sourceforge.net/project/webadmin/webmin/2.000/webmin_2.000_all.deb'
    )
    
    print(f"{updatePre} Installing 'Webmin'.")
    os.system("sudo dpkg -i webmin_2.000_all.deb")

    print(f"{updatePre} Configuring the firewall.")
    os.system("sudo ufw enable")
    os.system("sudo ufw allow 10000/tcp")

    # Firewall Reload
    print(f"{updatePre} Reloading the firewall.")
    os.system("sudo ufw reload")

    print(f"{updatePre} Enter a new root password for webmin.")
    passwrd = input(">")

    os.system(
        "sudo /usr/share/webmin/changepass.pl /etc/webmin root {0}".format(passwrd)
    )