from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import sys
from tkinter import *  
import tkinter as tk
import tkinter.ttk
import server2
#from server2 import connectionInit
import socket



import time 
import numpy as np 
from polishData import polishMyData
command=0
channel=2020

import matplotlib 
matplotlib.use("TkAgg")
from matplotlib import pyplot as pet
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
#import processData2
from processData2 import processMyData
from processData2 import ax,ay,az,Vix,Viy,xs,vx,vy
############################################Server code


def connectionInit():
	receivedData=open("receivedData.txt","a")
	receivedData.write("\n")
	global channel
	command=1
	print("port: ",channel)
	#channel = input('Channel:')
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
			#command=input("Enter command")
			if int(command) == 2 :
				active=False
				connect.send(b'0')
			elif int(command) ==1 :
				command=bytearray(str(command),'utf-8')
				connect.send(command)
				data=connect.recv(1024).decode()
				command=2
				if data:
					#receivedData.write("\n")
					#print("next line: ",data)
					receivedData.write(data)
					receivedData.write("\n")
					print("received data: ", data)
			else:
				print("waiting")

	finally:
		print("closing connection")
		#channel=channel+1
		receivedData.close()
		tServer.close()
############################################End of Server code


# Create the main window and Buttons 


def gui_start():
	global root
	root = tk.Tk()
	root.title("Explainable CamIoT")
	root.geometry("1500x800")

	def conTestFunc():
		return 5
	
	def close_window():
		root.quit()

	def restart():
		python = sys.executable
		os.excel(python,python,*sys.argv)

	def connection_pressed():
		connectionInit()
		polishMyData()

	def analysisFunc():
		result=processMyData()
		f = Figure(figsize=(2,2), dpi=100)
		axe = f.add_subplot(1, 1, 1)
		axe.clear()  
		axe.plot(xs,ax, label = "Ax")   
		axe.plot(xs,ay, label = "Ay")  
		axe.plot(xs,az, label = "Az")   
		axe.plot(xs,Viy, label = "Vy")
		axe.plot(xs,Vix, label = "Vx")
		axe.set_ylabel('acceleration') 
		axe.set_xlabel('time')
		axe.legend()
		canvas = FigureCanvasTkAgg(f, master=root)
		canvas.draw()
		canvas.get_tk_widget().grid(row=3,column=0,sticky=W)
		#canvas._tkcanvas.grid(row=3,column=0,sticky=W)
		resetButton.config(state="normal")
		anLabel=tk.Label(root,text=result,borderwidth=2, relief="solid")
		anLabel.grid(row=4,column=0,sticky=W)
    




	instLabel=tk.Label(root,text="Hit Record Data to begin. Then Follow the blinking LED to its permanent ON state and perform the gesture.")
	resLabel=tk.Label(root,text="To see your result then press Show My Analysis")
	conTestLabel=tk.Label(root,text="After you're done practicing the gesture. Click below for continious testing.")
	
	rdB=tk.Button(root, text="Record Data", command=connection_pressed)
	analysisB=tk.Button(root,text="Show My Analysis",command=analysisFunc)
	conTestB=tk.Button(root,text="continious Testing",command=conTestFunc)
	resetButton=tk.Button(root,text="Try Again",command=refresh,state=DISABLED)
	Exit = tk.Button(root, text="Exit the program", command = close_window)



	# Lay out label
	instLabel.grid(row=0,sticky=W)
	#instLabel.place(relx=0.01,rely=0.01)
	resLabel.grid(row=1,sticky=W)
	#resLabel.place(relx=0.01,rely=0.04)
	rdB.grid(row=2,column=0,sticky=W)
	#rdB.place(relx=0.01, rely=0.07)
	analysisB.grid(row=2,column=0)
	resetButton.place(relx=0.01,rely=0.9)
	Exit.place(relx=0.5,rely=0.9)

	tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=0, rowspan=5, sticky='ns')

	conTestLabel.grid(row=0,column=2,sticky=W+E)
	conTestB.grid(row=1,column=2)


	# Run forever!
	root.mainloop()

if __name__ == '__main__':
    def refresh():
        root.destroy()
        gui_start()

    gui_start()


