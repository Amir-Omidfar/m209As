
import socket
import time 
import numpy as np 

receivedData=open("receivedData.txt","a")
receivedData.write("\n")

def connectionInit():
	#channel = input('Channel:')
	channel = 8081
	########################
	time.sleep(2)
	tServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tServer.bind(('192.168.1.67', int(channel)))
	tServer.listen(0)
	connect,addr = tServer.accept()
	###############while loop for displaying the data
	
	active=True
	try:
		
		while active:
			command=input("Enter command")
			if int(command) == 2 :
				active=False
				connect.send(b'0')
			elif int(command) ==1 :
				command=bytearray(str(command),'utf-8')
				connect.send(command)
				data=connect.recv(1024).decode()

				if data:
					#receivedData.write("\n")
					#print("next line: ",data)
					receivedData.write(data)
					receivedData.write("\n")
					print("received data: ", data)
				
	finally:
		print("closing connection")
		tServer.close()
