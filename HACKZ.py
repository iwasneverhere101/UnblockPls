import os
import webbrowser
import time

def spam():
    while True:
        webbrowser.open("https://www.youtube.com/results?search_query=hentai_sexy")
        webbrowser.open("https://www.youtube.com/results?search_query=hentai_girls")
        webbrowser.open("https://www.youtube.com/results?search_query=hentai")


os.system('clear')
while True:
    print("-----------------------------------------------------------------------------")
    print(" H  H      /=\     |====|  || //  =====// ")
    print(" H  H     /   \    ||      ||//      //   ")
    print(" H--H    /  /\ \   ||      | |      //    ")
    print(" H  H   /  /-\  \  ||      ||\\    //     ")
    print(" H  H  /__/   \__\ |----|  || \\  //===== Made by Bigfatwormchips V.1.0")
    print("------------------------------------------------------------------------------")

 

                                                                                 
    print("***Welcome to HACKZ***")
    print("----------------------------------------------------------------")
    print("[MENU:]                                                        ")
    print("----------------------------------------------------------------")
    print("[TOR: Type 'tor1' first and then 'tor2' to download tor        ]")
    print("[SPAM: Type 'spam' to run a simple spam virus                  ]")
    print("[UPDATE SYSTEM: Type 'update' to update your system            ]")
    print("[EXIT: Type 'q' to exit                                        ] ")
    print("----------------------------------------------------------------")


    enter=input("Enter: ")

    if enter == "tor1":
        os.system('sudo echo "deb http://ftp.debian.org/debian bookworm main contrib" > /etc/apt/sources.list.d/cros.list')
        os.system('sudo apt-get update')
        os.system('sudo apt-get upgrade')
        time.sleep(2)
        os.system('clear')
        continue
    elif enter == "tor2":
        os.system('sudo echo "deb-src http://ftp.debian.org/debian bookworm main contrib" >> /etc/apt/sources.list.d/cros.list')
        os.system('sudo apt-get update')
        os.system('sudo apt-get upgrade')
        os.system('sudo apt-get install torbrowser-launcher')
        print("TOR BROWSER INSTALLED")
        time.sleep(3)
        os.system('clear')
        continue
    elif enter == "q":
        os.system('clear')
        break
    elif enter == "spam":
        spam()
        os.system('clear')
        continue
    elif enter == "update":
        os.system('sudo apt-get update')
        print("UPDATED SYSTEM")
        time.sleep(2)
        os.system('clear')
        
        continue
        
