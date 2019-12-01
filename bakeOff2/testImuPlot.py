#Authors: Amirali Omidfar, Hannaneh Hoajiji
from mpu6050 import mpu6050
sensor = mpu6050(0x68)

import time
from training import classifier
import numpy as np
# Hannaneh: importing the required module 
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animations

imuData = open("imuPredictData.csv","a")

active = True
counter = 0
label = ""
data= []
#Hannaneh
fig = plt.figure()
axe = fig.add_subplot(1, 1, 1)
xs = []
ax = []
ay = []
az = []
Viz = []
Xiz = []
while active:
    userInput=input("Enter E to exit otherwise P for predicting if the  gesture is triggering: \n")
    if userInput == "E":
        active=False
    else: 
        print("recording data")
        '''
        imuData.write("\n")
        imuData.write(label)
        imuData.write(", ")
        imuData.write(str(counter))
        imuData.write(", ")
        startTime=time.time()
        '''
        while len(data) < 42 : 
   #          accel_data = sensor.get_all_data()[0]
   #         # gyro_data = sensor.get_all_data()[1]

   #          data.append(accel_data['x'])
   #          data.append(accel_data['y'])
   #          data.append(accel_data['z'])
   #          '''
   #          data.append(gyro_data['x'])
   #          data.append(gyro_data['y'])
   #          data.append(gyro_data['z'])
   #          '''
   #          #Hannaneh
			# fig = plt.figure()
			# axe = fig.add_subplot(1, 1, 1)
			# xs = []
			# ys = []
			# xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
   #  		ys.append(accel_data['x'])
   #  		# Limit x and y lists to 20 items
		 #    xs = xs[-20:]
		 #    ys = ys[-20:]
		 #    # Format plot
		 #    plt.xticks(rotation=45, ha='right')
		 #    plt.subplots_adjust(bottom=0.30)
			# # plotting the line 1 points (Ax)  
			# plt.plot(x2, accel_data['x'], label = "Ax")
			# # plotting the line 2 points (Ay)  
			# plt.plot(x2, accel_data['y'], label = "Ay")
			# # plotting the line 3 points (Az)  
			# plt.plot(x2, accel_data['z'], label = "Az") 
			# # naming the x axis 
			# plt.xlabel('time') 
			# # naming the y axis 
			# plt.ylabel('accelerometer') 
			# # giving a title to my graph 
			# plt.title('accelerometer bundle') 
			# # show a legend on the plot 
			# plt.legend()   
			# Set up plot to call animate() function periodically
			ani = animation.FuncAnimation(fig, animate, fargs=(xs, ya, yy, yz), interval=1000)
			# function to show the plot 
			plt.show() 
            time.sleep(0.1)
        #data.pop()
        #data.pop()
        #data.pop()
        #data.pop()
        #data.pop()
        #data.remove(data[0])
        print("Initial shape of data: " ,len(data))
        newData=np.reshape(data,(1,-1))
        print("new Size ",newData.shape)
        result = classifier.predict(newData)
        print(result)
        data.clear()

#Hannaneh
# This function is called periodically from FuncAnimation
def animate(i, xs, ax, ay, az):
	accel_data = sensor.get_all_data()[0]

    data.append(accel_data['x'])
    data.append(accel_data['y'])
    data.append(accel_data['z'])
    '''
    data.append(gyro_data['x'])
    data.append(gyro_data['y'])
    data.append(gyro_data['z'])
    '''
    
	xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
	ax.append(accel_data['x'])
	ay.append(accel_data['y'])
	az.append(accel_data['z'])
	#v[i+1] = a[i](t[i+1] - t[i]) + v[i]
    #x[i+1] = v[i](t[i+1] - t[i]) + x[i]
    if i == 0:
    	Viz[i] = yz[i](xs[i] - 0) 
        Xiz[i] = Viz[i](xs[i] - 0) 
        Aiz = ax[i]
        Viz = Viz[i]
    else:
    	Viz[i] = yz[i](xs[i] - xs[i-1]) + Viz[i-1]
	    Xiz[i] = Viz[i](xs[i] - xs[i-1]) + Xiz[i-1]
	    Aiz = ax[i]
        Viz = Viz[i]

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ax = ax[-20:]
    ay = ay[-20:]
    az = az[-20:]

    # Draw x and y lists
    axe.clear()
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
	# plotting the line 1 points (Ax)  
	axe.plot(xs, ax, label = "Ax")
	# plotting the line 2 points (Ay)  
	axe.plot(xs, ay, label = "Ay")
	# plotting the line 3 points (Az)  
	axe.plot(xs, az, label = "Az") 
	# plotting the line 4 points (Vz)  
	axe.plot(xs, Viz, label = "Vz") 
	# naming the x axis 
	plt.xlabel('time') 
	# naming the y axis 
	plt.ylabel('accelerometer') 
	# giving a title to my graph 
	plt.title('accelerometer bundle') 
	# show a legend on the plot 
	plt.legend() 


