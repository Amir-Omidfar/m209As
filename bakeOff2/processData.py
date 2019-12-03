import csv
import datetime as dt
import matplotlib.pyplot as plt

fig = plt.figure()
axe = fig.add_subplot(1, 1, 1)
ax= []
ay= []
az= []
Vix = []
Viy = []
xs = []





def processMyData():
	#HH
	with open('polishedData.txt') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    Rows=list(csv_reader)
	    lastRow=Rows[-1]

	vx = 0
	vy = 0
	result=lastRow[42]
	print(lastRow[0])
	for j in range (14):
		if (j<14):
			ax.append(lastRow[3*j])
			ax[j]=float(ax[j])

			ay.append(lastRow[3*j+1])
			ay[j]=float(ay[j])

			az.append(lastRow[3*j+2])
			az[j]=float(az[j])

			Viy.append(ay[j]*(0.1) + vy)
			vy = Viy[j]

			Vix.append(ax[j]*(0.1) + vx)
			vx = Vix[j]

			xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
		        
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
	axe.plot(xs, Viy, label = "Vy") 
	# naming the x axis 
	axe.plot(xs, Vix, label = "Vx") 
	plt.xlabel('time') 
	# naming the y axis 
	plt.ylabel('accelerometer') 
	# giving a title to my graph 
	plt.title('accelerometer bundle') 
	# show a legend on the plot 
	print("Here is your classification resutl:" ,result)
	plt.legend()
	plt.show()
	csv_file.close()


#processMyData()

