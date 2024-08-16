import os
import time
print("===========================================")
print("HACKZ INSTALLER")
print("===========================================")
print("Type 'install' to install the requirements and run HACKZ latest version. ")
enter = input("Enter : ")
while True:
    if enter == "install":
        os.system('sudo apt-get update')
        os.system('sudo apt-get upgrade')
        os.system('sudo apt-get install python3-pip')
        os.system('sudo pip3 install -r requirements.txt --break-system-packages')
        os.system('sudo python3 HACKZ.py')
    else:
        print("ERROR. COULD NOT UNDERSTAND")
        continue
