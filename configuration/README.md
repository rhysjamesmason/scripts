# About this directory

In this directory, you will input a config file for the script to use to configure your linux system to the speciforcation given to you. Please note that not all processes will be covered by this program and will require the users input.

## Config example

```json
{
    "PermitRootLogin": false, // Want people to login as root?
    "AllowGuestUserAccounts": false, // Do you allow a guest account?
    "AuthUsers": [
        {
            "username": "john",
            "admin": true,
        },
        // {
        //     "username": "steve",
        //     "admin": false,
        // },
    ],
    "AllowAnyoneSudo": false, // Allow anyone to use sudo
    "RemoveAllNonWorkTools": true, // Removes non work related tools
    "PasswordExp": {
        "PassMinDay": 7, 
        "PassMaxDay": 90,
        "PassWarnDay": 14, 
    }
}
```