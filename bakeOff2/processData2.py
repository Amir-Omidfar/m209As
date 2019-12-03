import csv
import datetime as dt
import numpy as np
import random


ax= []
ay= []
az= []
Vix = []
Viy = []
xs = []
vx = 0
vy = 0
correct=["you did it right congrats!!","Excellent! That was the proper gesture",
"Well done! You successfully triggered the device","Yup that's right!","Nicely triggered. Good job!"]

incorrect=["Almost no arm movement detected. You need to be more active",
"Come on CamIoT is a mind reader.You need to move your arm",
"Seems to me that you started early this time. Follow the LED carfeully",
"Looks like you're falling behind, initiate your move right away when the LED is solid",
"You need to perform the gesture faster",
"You're too fast, next round you need to slow down"]

def feedback(result):
	if result ==" '[ True]'":
		return random.choice(correct)
	elif result ==" '[False]'":
		return random.choice(incorrect)


def processMyData():
	#HH
	with open('polishedData.txt') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    Rows=list(csv_reader)
	    lastRow=Rows[-1]

	
	#global ax,ay,az,Vix,Viy,xs,vx,vy
	vx = 0
	vy = 0
	rawData=lastRow[42]
	result=feedback(str(rawData))
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
			#timeStamp=dt.datetime.now().strftime('%-S.%f')
			#timeStampRounded=timeStamp[:-3]
			#xs.append(timeStamp)
			xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
		        

	csv_file.close()
	return result


