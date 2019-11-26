import tkinter as tk
import server2
from server2 import recordData,sequence,result




# Create the main window
root = tk.Tk()
root.title("Explainable CamIoT")
root.geometry("500x500")

# Create label
label = tk.Label(root, text="Data Recording: ")

B = tk.Button(root, text ="Press the button to record data", command = recordData)

# Lay out label
label.pack()
B.place(x=50, y=10)
# Run forever!

root.mainloop()




