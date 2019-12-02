import tkinter as tk
import server2
from server2 import recordData



#HH Parameters
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
#HH

# Create the main window
root = tk.Tk()
root.title("Explainable CamIoT")
root.geometry("500x500")

# Create label
label = tk.Label(root, text="Data Recording: ")

def close_window():
	root.quit()


B = tk.Button(root, text ="Press the button to record data", command = recordData)
Exit = tk.Button(root, text="Exit the program", command = close_window)

#HH
with open('receivedData.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    Rows=list(csv_reader)
	Tot_rows=len(Rows)
with open('receivedData.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
    	if line_count==Tot_rows:
    		Viy = 0
    		Vix = 0
    		for j in range (15)
			if (j<14):
				ax[j]=row[3*j]
				ay[j]=row[3*j+1]
				az[j]=row[3*j+2]
				Viy[j] = ay[j]*(0.1) + Viy
			    Xiy[j] = Viy[j]*(0.1) + Xiy[j-1]
		        Viy = Viy[j]
		        Vix[j] = ax[j]*(0.1) + Vix
			    Xiy[j] = Vix[j]*(0.1) + Xix[j-1]
		        Vix = Vix[j]


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
				plt.xlabel('time') 
				# naming the y axis 
				plt.ylabel('accelerometer') 
				# giving a title to my graph 
				plt.title('accelerometer bundle') 
				# show a legend on the plot 
				plt.legend()
			else: 
				print(f'Classified as {row[14]}.')

		plt.show()
		line_count+=1
#HH

# Lay out label
label.pack()
B.place(x=50, y=40)
Exit.place(x=40, y=350)

# Run forever!

root.mainloop()
