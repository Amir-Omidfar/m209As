from mpu6050 import mpu6050
sensor = mpu6050(0x68)

import time
#from training import classifier
from joblib import dump,load
import numpy as np

import RPi.GPIO as GPIO
from time import sleep
GPIO.setwar


classifier = load ('/home/pi/Desktop/trigger/triggerTrain.joblib')

def imuTri():
  imuData = open("imuPredictData.csv","a")
  
  active = True
  counter = 0
  label = ""
  data= []
  print("Recording Data")
  while active:
        while len(data) < 42 : 
            accel_data = sensor.get_all_data()[0]
           # gyro_data = sensor.get_all_data()[1]
  
            data.append(accel_data['x'])
            data.append(accel_data['y'])
            data.append(accel_data['z'])
            '''
            data.append(gyro_data['x'])
            data.append(gyro_data['y'])
            data.append(gyro_data['z'])
            '''
            time.sleep(0.1)
        newData=np.reshape(data,(1,-1))
        result = classifier.predict(newData)
        #print(result)
        if result:
            print("True")
            return True
        
        for k in range(3):
          data.pop(0)
        #data.clear()

while True:
  imuTri()
#imuTri()
