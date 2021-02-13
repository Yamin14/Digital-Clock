from tkinter import *
from datetime import datetime

root = Tk()
root.config(background="black")

frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def update_time():
	time = str(datetime.now())[11:13] + "\n" + str(datetime.now())[14:16] + "\n" + str(datetime.now())[17:19]
	time_label.config(text=time)
	root.after(1000, update_time)
	
time_label = Label(frame, bg="black", fg="cyan", font=("Comic Sans MS", 70))
time_label.pack()

update_time()

root.mainloop()
