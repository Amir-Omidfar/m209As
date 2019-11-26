import socket
import time 

channel = input('Channel:')
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
		data=connect.recv(1024).decode()
		if data:
			li = list(data.split(",")) 
			#print(data[41])
			#print(li[41])
			if (len(li) > 41):
				print(li[40])
		else:
			active=False
		

finally:
        tServer.close()

