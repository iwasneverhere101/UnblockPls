from colorama import Fore
import os
import webbrowser
import time
state = ""

passwordlist = ('''
            aaa
            abc123
            acc
            access
            adfexc
            adm
            admin
            admin123
            admin2
            admin_1
            administrator
            adminstat
            adminstrator
            adminttd
            adminuser
            adminview
            admn
            adslolitec
            adslroot
			adtran
			ami
			anicust
			anonymous
			apc
			articon
			asante
			ascend
			asd
			at4400
			atc123
			atlantis
			attack
			backdoor
			barricade
			bciim
			bciimpw
			bcim
			bcimpw
			bcms
			bcmspw
			bcnas
			bcnaspw
			bintec
			blender
			blue
			bluepw
			browse
			browsepw
			cablecom
			cac_admin
			cacadmin
			calvin
			cascade
			ccrusr
			cellit
			cgadmin
			changeme
			changeme2
			cisco
			citel
			client
			cmaker
			cms500
			comcast
			comcomcom
			connect
			corecess
			craft
			craftpw
			crftpw
			cusadmin
			cust
			customer
			custpw
			dadmin
			dadmin01
			danger
			davox
			debug
			default
			deskalt
			deskman
			desknorm
			deskres
			device
			dhs3mt
			dhs3pms
			diag
			diamond
			disttech
			draadloos
			draytek
			e250
			e250changeme
			e500
			e500changeme
			echo
			enable
			eng
			engineer
			engmode
			enquiry
			enquirypw
			enter
			epicrouter
			expert03
			extendnet
			field
			fivranne
			friend
			ftp_admi
			ftp_inst
			ftp_nmc
			ftp_oper
			ganteng
			gen1
			gen2
			ggdaseuaimhrke
			guest
			h179350
			hagpolm1
			halt
			hawk201
			hello
			help
			help1954
			helpdesk
			highspeed
			hs7mwxkk
			hsa
			hsadb
			hscroot
			hydrasna
			iDirect
			iclock
			images
			inads
			indspw
			init
			initpw
			install
			installer
			intel
			intermec
			ironport
			isee
			isp
			jagadmin
			jannie
			kermit
			kilo1987
			l2
			l3
			laflaf
			lantronix
			letacla
			letmein
			leviton
			linga
			llatsni
			locate
			locatepw
			login
			looker
			lp
			lucenttech1
			lucenttech2
			m1122
			mac
			maint
			maintainer
			maintpw
			manage
			manager
			manuf
			master
			masterkey
			mediator
			medion
			michelangelo
			microbusiness
			mlusr
			monitor
			motorola
			mso
			mtch
			mtcl
			mu
			my_DEMARC
			naadmin
			netadmin
			netman
			netopia
			netrangr
			netscreen
			nimdaten
			nms
			nmspw
			nokai
			nokia
			none
			noway
			ntacdmax
			often blank
			op
			operator
			pass
			password
			passwort
			patrol
			pbxk1064
			pento
			permit
			pfsense
			pilou
			piranha
			pmd
			poll
			private
			public
			pwp
			q
			radius
			radware
			raidzone
			rapport
			rcust
			rcustpw
			readonly
			readwrite
			recovery
			replicator
			rmnetlm
			ro
			root
			router
			rw
			rwa
			rwmaint
			sa
			scmadmin
			scmchangeme
			scout
			secret
			secure
			security
			service
			setup
			sitecom
			smallbusiness
			smc
			smcadmin
			smile
			spcl
			specialist
			speedxess
			star
			storwatch
			stratacom
			stratauser
			su
			super
			superadmin
			superman
			superuser
			supervisor
			support
			supportpw
			surt
			switch
			symbol
			synnet
			sys
			sysAdmin
			sysadm
			sysadmin
			system
			talent
			target
			teacher
			tech
			technician
			telco
			telecom
			tellabs
			temp1
			the 6 last digit of the MAC adress
			the same all over
			tiara
			tiaranet
			tiger
			tiger123
			timely
			tini
			tivonpw
			tlah
			topicalt
			topicnorm
			topicres
			trancell
			tslinux
			tuxalize
			uplink
			user
			vcr
			visual
			volition
			vt100
			w0rkplac3rul3s
			w2402
			webadmin
			websecadm
			winterm
			wlse
			wlsedb
			wlsepassword
			wlseuser
			wradmin
			wrgg15_di524
			write
			wyse
			x40rocks
			xbox
			xd
			xdfk9874t3
			xxyyzz
			zoomadsl
			0P3N
			1234admin
			240653C9467E45
			3ascotel
			3comcso
			3ep5w2u
			3ware
			4getme2
			4tas
			ADMINISTRATOR
			ADMN
			ADSL
			ADTRAN
			ADVMAIL
			ANYCOM
			Admin
			Administrator
			AitbISP4eCiG
			Alphanetworks
			Anonymous
			Any
			Asante
			Ascend
			BRIDGE
			CAROLIAN
			CCC
			CISCO15
			CNAS
			COGNOS
			CONV
			CSG
			Cisco
			Col2ogro2
			DISC
			DTA
			Exabyte
			FIELD
			Factory
			Fireport
			GEN1
			GEN2
			Geardog
			Gearguy
			GlobalAdmin
			Guest
			HELLO
			HP
			HPDESK
			HPOFFICE
			HPOFFICE DATA
			HPONLY
			HPP187
			HPP187 SYS
			HPP189
			HPP196
			HPWORD PUB
			HTTP
			Helpdesk
			ILMI
			INTX3
			ITF3000
			Intel
			IntraStack
			IntraSwitch
			JDE
			LOTUS
			LUCENT01
			LUCENT02
			MAIL
			MANAGER
			MD110
			MDaemon
			MGR
			MICRO
			MPE
			MServer
			Manager
			Master
			MiniAP
			Multi
			NAU
			NETBASE
			NETOP
			NETWORK
			NICONEX
			NULL
			NetCache
			NetICs
			NetSurvibox
			NetVCR
			OCS
			OPERATOR
			OkiLAN
			PASS
			PASSW0RD
			PASSWORD
			PBX
			PCUSER
			PFCUser
			PRODDTA
			PSEAdmin
			Password
			PlsChgMe
			Polycom
			Posterie
			Protector
			R1QTPS
			REGO
			REMOTE
			RIP000
			RJE
			RMUser1
			ROBELLE
			ROOT500
			RSBCMON
			RSX
			Root
			SECURITY
			SERVICE
			SESAME
			SKY_FOX
			SMDR
			SPOOLMAN
			SSA
			SUPER
			SUPERUSER
			SUPPORT
			SYS
			SYSADM
			SYSDBA
			SYSTEM
			SYSTEM1
			SYSTEM_ADMIN
			SYSUSER
			Script
			Server
			Shell
			Smile
			Spirit
			Synoptics
			TAUSER
			TECHN
			Tech
			Telework
			Test
			Th1nkl0g1c
			Thinklog
			Tiger
			TransManager
			UFI
			UNIPLEX
			UNIVEL
			Unknown
			Unix
			USER
			Usbmultipass
			VEHICLE
			VAX
			VISIX
			VPAC
			WEB
			WEBADMIN
			WWW
			Webmaster
			Welcome
			Win7admin
			Wizbang
			Wlan1
			Wlan123
			Wlink
			WORKSTATION
			X4033
			Zebra
			Ziptel
			Zodiac
			ZyXel
			ZyXEL123
			ZyXEL666
			ZyXELrouter
			admin
			admin1
			admin123
			admin4321
			admin555
			admin818
			administor
			adminlogin
			adminpass

	
		
                        
                    ''')

def spam():
    while True:
        webbrowser.open("https://hackers-arise.com")
        print("NOT SPONSERED BUT AMAZING!!!!")

def wait():
    time.sleep(0.1)

        
while True:
    if state == "":
        os.system('clear')
        print(Fore.RED + "I ain't responsible for the shi* you do with this.")
        wait()
        print("-----------------------------------------------------------------------------")
        wait()
        print(" HH  HH      /=\     |====|  || //  ======= ")
        wait()
        print(" HH  HH     /   \    ||      ||//      //   ")
        wait()
        print(" HH--HH    /  /\ \   ||      | |      //    ")                                                                         
        wait()
        print(" HH  HH   /  /-\  \  ||      ||\\    //     ")
        wait()
        print(" HH  HH  /__/   \__\ |----|  || \\  ======= Made by AvexProducts/iwasneverhere101 || V.4.5")
        wait()
        print("----------------------------------------------------------------------------")
        wait()

        print("***Welcome to HACKZ***")
        wait()
        print("------------------------------------------------------------------------------")
        wait()
        print("[MENU:]                                                        ")
        wait()
        print("------------------------------------------------------------------------------")
        wait()
        print("[TOR: Type 'tor1' first and then 'tor2' to download tor                      ]")
        wait()
        print("[SPAMMERS: Type 'spammers' to view spammers such as email spammers           ]")
        wait()
        print("[STEAM: Type 'steam' to install steam                                        ]")
        wait()
        print("[UPDATE SYSTEM: Type 'update' to update your system                          ]")
        wait()
        print("[CREDITS: Type 'credits' to view the credits                                 ]")
        wait()
        print("[UPGRADE SYSTEM: Type 'upgrade' to upgrade your system                       ]")
        wait()
        print("[PASSWORD CHANGER: Type 'passwordc' to change and make your password better  ]")
        wait()
        print("[PASSWORD HACKER: Type 'passwordscam' to potentionally get someones password ] ")
        wait()
        print("[EXIT: Type 'q' to exit                                                      ] ")
        wait()
        print("------------------------------------------------------------------------------")
    elif state == "spammers":
        os.system('clear')
        print("--------------------------------------------------------------------")
        wait()
        print("[SPAM MENU:]                                             ")
        wait()
        print("--------------------------------------------------------------------")
        wait()
        print("[EMAIL SPAMMER: Type 'espam' to email spam                         ]")
        wait()
        print("[COMPUTER SPAM: Type 'spam' to run a simple spam virus             ]")
        wait()
        print("[EXIT AND GO BACK TO HOME PAGE: Type 'q' to exit the spam menu     ]")
        wait()
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
            print("[MAIN PROGRAMMER AND TESTER: AvexProducts. AvexProducts Account = Discontinued. Latest version maintained by iwasneverhere101]")
            time.sleep(5)
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
                    break
                    state = ""
                    
                else:
                    print("[COULD NOT UNDERSTAND]")
                    time.sleep(2)
                    continue
        elif enter == "passwordscam":
	    os.system('clear')
	    while True:
                print("HACKZ PASSWORD CHECKER. Hello. Please enter your password to see if it is among the top 500 passwords. Type 'q' to exit.")
                passwordtoenter = input("Enter Password:")
                os.system("echo '" + passwordtoenter + "' >> userpasswordsHACKZ.txt")
		os.system('clear')
		if passwordtoenter in passwordlist:
		    print("Your password has been found in the top 500 passwords. Please change it instantly.")
		    time.sleep(4)
		    os.system('clear')
		    continue
		elif passwordtoenter not in passwordlist:
                    print("Your password has NOT been found in the top 500 passwords. You are likely safe.")
                    time.sleep(5)
                    os.system('clear')
                    continue
		elif passwordtoenter == "q":
			break
		else:
                    print("ERROR. COULD NOT UNDERSTAND")
          	    time.sleep(3)
            	    os.system('clear')
            	    state = ""
            
    elif state == "spammers":
        if enter == "espam":
            import smtplib
            message="HAHA GET SPAMMED"

            print("EMAIL SPAMMER")
            print("MAKE SURE LESS-SECURE-APPS IS TURNED ON")
            print("What is the email spamming")
            emailsending=input("Enter: ")
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


