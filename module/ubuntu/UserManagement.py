import os

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