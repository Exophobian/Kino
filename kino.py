import time
import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

time.sleep(1)
os.system("clear")

print("\u001b[36m		┈┈┈╲┈┈┈┈╱") #introduction
print("		-┈┈╱▔▔▔▔╲")
print("		┈┈┃┈▇┈┈▇┈┃")
print("		╭╮┣━━━━━━┫╭╮")
print("		┃┃┃┈┈┈┈┈┈┃┃┃")
print("		╰╯┃┈┈┈┈┈┈┃╰╯")
print("		┈┈╰┓┏━━┓┏╯")
print("		┈┈┈╰╯┈┈╰╯ \u001b[37mKino Developed By Exo")

time.sleep(2)
os.system("clear")

print("")
print("\u001b[36m		██╗  ██╗██╗███╗   ██╗ ██████╗")
print("		██║ ██╔╝██║████╗  ██║██╔═══██╗")
print("		█████╔╝ ██║██╔██╗ ██║██║   ██║")
print("		██╔═██╗ ██║██║╚██╗██║██║   ██║")
print("		██║  ██╗██║██║ ╚████║╚██████╔╝")
print("		╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝")
time.sleep(2)
print("\u001b[37m       		Multi-Tool     ")
print("")
time.sleep(1)

name = input("Hello, i am KINO. who are you? \nInsert Name: ") #insert name
if name == "":
	print("Please enter a valid name")
else:
	os.system("clear")
print("")
print("\u001b[36m		██╗  ██╗██╗███╗   ██╗ ██████╗")
print("		██║ ██╔╝██║████╗  ██║██╔═══██╗")
print("		█████╔╝ ██║██╔██╗ ██║██║   ██║")
print("		██╔═██╗ ██║██║╚██╗██║██║   ██║")
print("		██║  ██╗██║██║ ╚████║╚██████╔╝")
print("		╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝")
print('\u001b[37m		hello',name,'welcome')
print("		Here are your options")
print("")
print("")
print("		1. Portscan		2. Ping")
print("")
print("		3. Credits		4. DDoS")
print("")
option = input("Select: ")
if option == "1":
		print("\u001b[36m		You have selected Portscan") #portscanner
		os.system("clear")
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
	print("\u001b[36mGo buy luminous security team panel from me or @luminous_security_team on instagram")
