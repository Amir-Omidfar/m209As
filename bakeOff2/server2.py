import socket
import time 
import numpy as np 
global sequence
global result

counter=1
receivedData=open("receivedData.txt","a")


def recordData():
	#channel = input('Channel:')
	channel = 8080
	########################
	time.sleep(2)
	tServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tServer.bind(('192.168.1.67', int(channel)))
	tServer.listen(0)
	connect,addr = tServer.accept()
	###############while loop for displaying the data
	sequence=[]
	active=True
	try:
		#connect.send(b'1')
		while active:
			command=input("Enter command")
			command=bytearray(str(command),'utf-8')
			connect.send(command)
			data=connect.recv(1024).decode()

			if data:
				if data == "2":
					receivedData.write("\n")
					print("next line: ",data)
					++counter
				else:
					receivedData.write(str(counter))
					receivedData.write(", ")
					receivedData.write(data)
					print("received data: ", data)
					

	finally:
	        tServer.close()

