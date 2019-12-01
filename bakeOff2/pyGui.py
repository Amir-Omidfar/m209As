import tkinter as tk
import server2
from server2 import recordData

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



# Lay out label
label.pack()
B.place(x=50, y=40)
Exit.place(x=40, y=350)

# Run forever!

root.mainloop()




