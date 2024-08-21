from colorama import Fore
import os
import webbrowser
import time
state = ""

def spam():
    while True:
        webbrowser.open("https://hackers-arise.com")
        print("NOT SPONSERED BUT AMAZING!!!!")

        
while True:
    if state == "":
        os.system('clear')
        print(Fore.RED + "I ain't responsible for the shi* you do with this.")
        print("-----------------------------------------------------------------------------")
        print(" HH  HH      /=\     |====|  || //  ======= ")
        print(" HH  HH     /   \    ||      ||//      //   ")
        print(" HH--HH    /  /\ \   ||      | |      //    ")
        print(" HH  HH   /  /-\  \  ||      ||\\    //     ")
        print(" HH  HH  /__/   \__\ |----|  || \\  ======= Made by AvexProducts || V.2.0")
        print("----------------------------------------------------------------------------")

        print("***Welcome to HACKZ***")
        print("----------------------------------------------------------------------------")
        print("[MENU:]                                                        ")
        print("----------------------------------------------------------------------------")
        print("[TOR: Type 'tor1' first and then 'tor2' to download tor                    ]")
        print("[SPAMMERS: Type 'spammers' to view spammers such as email spammers         ]")
        print("[STEAM: Type 'steam' to install steam                                      ]")
        print("[UPDATE SYSTEM: Type 'update' to update your system                        ]")
        print("[CREDITS: Type 'credits' to view the credits                               ]")
        print("[UPGRADE SYSTEM: Type 'upgrade' to upgrade your system                     ]")
        print("[PASSWORD CHANGER: Type 'passwordc' to change and make your password better]")
        print("[EXIT: Type 'q' to exit                                                    ] ")
        print("----------------------------------------------------------------------------")
    elif state == "spammers":
        os.system('clear')
        print("--------------------------------------------------------------------")
        print("[SPAM MENU:]                                             ")
        print("--------------------------------------------------------------------")
        print("[EMAIL SPAMMER: Type 'espam' to email spam                         ]")
        print("[COMPUTER SPAM: Type 'spam' to run a simple spam virus             ]")
        print("[EXIT AND GO BACK TO HOME PAGE: Type 'q' to exit the spam menu     ]")
        print("--------------------------------------------------------------------")

    enter=input("Enter: ")

    if state == "":
        if enter == "tor1":
            os.system('sudo echo "deb http://ftp.debian.org/debian bookworm main contrib" > /etc/apt/sources.list.d/cros.list')
            os.system('sudo apt-get update')
            os.system('sudo apt-get upgrade')
            time.sleep(2)
            os.system('clear')
            state=""
        elif enter == "tor2":
            os.system('sudo echo "deb-src http://ftp.debian.org/debian bookworm main contrib" >> /etc/apt/sources.list.d/cros.list')
            os.system('sudo apt-get update')
            os.system('sudo apt-get upgrade')
            os.system('sudo apt-get install torbrowser-launcher')
            print("TOR BROWSER INSTALLED")
            time.sleep(3)
            os.system('clear')
            state=""
        elif enter == "q":
            os.system('clear')
            break
        elif enter == "update":
            os.system('sudo apt-get update')
            print("SYSTEM UPDATED")
            time.sleep(2)
            os.system('clear')
            state=""
        elif enter == "spammers":
            state="spammers"

        elif enter == "upgrade":
            os.system('sudo apt-get upgrade')
            print("SYSTEM UPGRADED")
            time.sleep(2)
            os.system('clear')
            state=""
        elif enter == "credits":
            print("[MAIN PROGRAMMER AND TESTER: AvexProducts]")
            time.sleep(2)
            os.system('clear')
            state=""
        #CONTINUE THIS
        elif enter == "steam":
            os.system('sudo apt-get update')
            os.system('sudo apt-get upgrade')
            os.system('sudo apt-get install flatpak')
            os.system('sudo apt-get install xorg')
            os.system('sudo wget https://dl.flathub.org/repo/appstream/com.valvesoftware.Steam.flatpakref')
            os.system('sudo flatpak install com.valvesoftware.Steam.flatpakref')
            time.sleep(4)
            print("STEAM IS INSTALLED.")
            time.sleep(2)
            state = ""
        elif enter == "passwordc":
            import os
            import time
            while True:
                print("=============================")
                print("HACKZ PASSWORD RANDOMIZER")
                print("=============================")
                print("[ENTER YOUR PASSWORD AND IT WILL BECOME STRONGER: ")
                passwordchange = input("[ENTER: ")
                passwordchange = passwordchange.replace("a", "b")
                passwordchange = passwordchange.replace("c", "d")
                passwordchange = passwordchange.replace("e","f")
                passwordchange = passwordchange.replace("g", "h")
                passwordchange = passwordchange.replace("i", "j")
                passwordchange = passwordchange.replace("k", "l")
                passwordchange = passwordchange.replace("m", "n")
                passwordchange = passwordchange.replace("o", "p")
                passwordchange = passwordchange.replace("q", "r")
                passwordchange = passwordchange.replace("s", "t")
                passwordchange = passwordchange.replace("u", "v")
                passwordchange = passwordchange.replace("w", "x")
                passwordchange = passwordchange.replace("y", "z")
                passwordchange = passwordchange.replace("b", "e")
                print("YOUR NEW PASSWORD IS: ")
                print(passwordchange)
                choice = input("Would you like to enter a new password? Y/N (MAKE SURE YOUR ANSWER IS CAPITALIZED): ")
                if choice == "Y":
                    continue
                elif choice == "N":
                    print("LEAVING...")
                    time.sleep(2)
                    state = ""
                    
                else:
                    print("[COULD NOT UNDERSTAND]")
                    time.sleep(2)
                    continue

        else:
            print("ERROR. COULD NOT UNDERSTAND")
            time.sleep(3)
            os.system('clear')
            state=""
            
    elif state == "spammers":
        if enter == "espam":
            import smtplib
            message="GYATT"

            print("EMAIL SPAMMER")
            print("MAKE SURE LESS-SECURE-APPS IS TURNED ON")
            print("What is the email spamming")
            emailsending=input("Enter:")
            print("What is the email being spammed")
            emailspammed=input("Enter :")
            print("What is the email spamming password?")
            password=input("Enter: ")

            while True:
                with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
                    smtpserver.ehlo()
                    smtpserver.starttls()
                    smtpserver.ehlo()
                    smtpserver.login(emailsending, password)
                    while True:
                        smtpserver.sendmail(emailsending, emailspammed, message)
                        print("SPAMMING. PRESS 'CTRL+Z' TO STOP THE SPAM.")
                        continue
        elif enter == "spam":
            spam()
            os.system('clear')
            state="spammers"
        elif enter == "q":
            print("LEAVING SPAM MENU")
            time.sleep(2)
            os.system('clear')
            state=""


