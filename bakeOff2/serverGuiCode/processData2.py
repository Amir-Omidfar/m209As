#Team:Amirali Omidfar, Hannaneh Hojaiji
#Source for text to speech conversion https://pypi.org/project/pyttsx3/
import csv
import datetime as dt
import numpy as np
import random


ax= []
ay= []
az= []
Vix = []
Viy = []
Viz = []
xs = []
vx = 0
vy = 0
vz = 0


minAx=0
minAy=0
minAz=0
minVx=0
minVy=0

maxAx=0
maxAy=0
maxAz=0
maxVx=0
maxVy=0
correct=["you did it right congrats!!","Excellent! That was the proper gesture",
"Well done! You successfully triggered the device","Yup that's right!","Nicely triggered. Good job!"]

slowDown=["Seems to me that you started early this time. Follow the LED carfeully",
"You're too fast, next round you need to slow down", "oh oh, too fast!"]

speedUp=["You need to perform the gesture faster","Almost no arm movement detected. You need to be more active",
"Come on CamIoT is a mind reader.You need to move your arm",
"Looks like you're falling behind, initiate your move right away when the LED is solid"]

tryAgain=["Please try again", "Hmm, something went wrong, please try again."]

def feedback(result):
	if result ==" '[ True]'":
		return 1.0 #random.choice(correct)
	elif result ==" '[False]'":
		return 0.0 #random.choice(incorrect)


def processMyData():
	#HH
	with open('polishedData.txt') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    Rows=list(csv_reader)
	    lastRow=Rows[-1]

	
	global ax,ay,az,Vix,Viy,Viz,xs,vx,vy,vz
	vx = 0
	vy = 0
	vz = 0
	rawData=lastRow[42]
	#result=feedback(str(rawData))
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

			Viz.append(az[j]*(0.1) + vz)
			vz = Viz[j]
			#timeStamp=dt.datetime.now().strftime('%-S.%f')
			#timeStampRounded=timeStamp[:-3]
			#xs.append(timeStamp)
			xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
	csv_file.close()
	minAx=min(ax)
	minAy=min(ay)
	minAz=min(az)
	minVx=min(Vix)
	minVy=min(Viy)

	maxAx=max(ax)
	maxAy=max(ay)
	maxAz=max(az)
	maxVx=max(Vix)
	maxVy=max(Viy)

	if ((minAx<-15.0 and maxAx>-2.0) and (feedback(str(rawData))==1.0)):
		result=random.choice(slowDown)

	elif ((-15.0<minAx<-8.0 and -4.0<maxAx<0.0) and (feedback(str(rawData))==1.0)):
		result=random.choice(correct)

	elif ((minAx<-15.0 and maxAx>-2.0) and (feedback(str(rawData))==0.0)):
		result=random.choice(slowDown)

	elif ((-8.0<minAx<-15.0 and -4.0<maxAx<0.0) and (feedback(str(rawData))==0.0)):
		result=random.choice(tryAgain)

	else:
		result=random.choice(speedUp)

	if feedback(str(rawData))==0.0 :
		ans="Classification Result: No Trigger detected\nFeedback: "
	else:
		ans="Classification Result: Trigger detected\nFeedback: "
	return ans+result


