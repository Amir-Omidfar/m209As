import socket
import time 
global sequence
global result

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
		connect.send(b'1')
		while active:
			data=connect.recv(1024).decode()
			if data:
				li = list(data.split(",")) 
				if (len(li) > 41):
					#print(li[40])
					sequence=data
				else :
					#print(data)
					result=data
			else:
				active=False
		print(sequence)
		print(result)	
		return sequence,result

	finally:
	        tServer.close()

