
import socket
import time 


def connection():
	#channel = input('Channel:')
	channel = 4040
	########################
	time.sleep(2)
	tServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tServer.bind(('192.168.1.67', int(channel)))
	tServer.listen(0)
	connect,addr = tServer.accept()
	###############while loop for displaying the data
	print(connect)
	print(addr)
	
	active=True
	try:
		while True:
			t=2+2
	finally:
		print("closing connection")
		tServer.close()
	









