import io
import socket
import struct
import time

from mpu6050 import mpu6050
sensor = mpu6050(0x68)
#from training import classifier
from joblib import dump,load
import numpy as np



##########Server SetUp
channel = input('channel: ')
# Make a file-like object out of the connection
time.sleep(3)
tSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tSocket.connect(('192.168.1.67', int(channel)))

classifier = load ('/home/pi/Desktop/trigger/triggerTrain.joblib')


try:
    imuData = open("imuPredictData.csv","a")
    active = True
    counter = 0
    label = ""
    data= []
    print("Start recording")
    while active:
        while len(data) < 42 : 
            accel_data = sensor.get_all_data()[0]

            data.append(accel_data['x'])
            data.append(accel_data['y'])
            data.append(accel_data['z'])
            time.sleep(0.1)

        newData=np.reshape(data,(1,-1))

        result = classifier.predict(newData)
        print(result)
        if result:
            print("good job!")
            tSocket.send(b'1')
            for k in range (15):
                data.pop(0)
        else:
            for k in range(6):
                data.pop(0)



finally:
    connection.close()
    client_socket.close()
    tSocket.close()
