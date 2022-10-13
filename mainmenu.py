
import tkinter as tk
from turtle import bgcolor
import sys
import subprocess
#import errno

#from . import admin

#from tkinter import ttk

try:

    master = tk.Tk()

    master.title("Sleep Detection Monitoring Software")
    master.geometry("")


    l = tk.Label(master, text = "Sleep Detection Monitoring Software", font = ("Times New Roman", 15), fg = "Black")
    l.pack()

    def startclobby():

        frame1.pack_forget()
        
        frame2.pack(anchor = tk.CENTER)
        back["state"] = "active"

    def startjlobby():

        frame1.pack_forget()
        
        frame3.pack(anchor = tk.CENTER)
        back["state"] = "active"

    def goback():

        frame2.pack_forget()
        frame3.pack_forget()

        frame1.pack(anchor = tk.CENTER)
        back["state"] = "disabled" 

    def makelobby():

        global lole1

        

        if (e1.index("end") == 0):

            tk.messagebox.showwarning("Lobby should have a name!")

        else:
            
            lole1 = e1.get()
            master.destroy()
            subprocess.call([sys.executable, "admin.py"])
        
            


            

    

    frame1 = tk.Frame(master)
    frame2 = tk.Frame(master)
    frame3 = tk.Frame(master)

    back = tk.Button(master, text = "Back", bg = "Red", fg = "White", state = "disabled", command = lambda: goback())
    back.pack(anchor = tk.SW, side = tk.BOTTOM)

    exit = tk.Button(master, text = "Exit", bg = "Red", fg = "White", command = exit)
    exit.pack(anchor = tk.SE, side = tk.BOTTOM)


    b1 = tk.Button(frame1, text = "Create Lobby", bg = "Black", fg = "White", command = lambda: startclobby())
    b1.grid(row = 0, column = 0)

    b2 = tk.Button(frame1, text = "Join Lobby", bg = "Black", fg = "White", command = lambda: startjlobby())
    b2.grid(row = 0, column = 1)


    b3 = tk.Button(frame2, text = "Make Lobby", bg = "Black", fg = "White", command = lambda: makelobby())
    b3.grid(row = 1, column = 0)


    e1 = tk.Entry(frame2)
    e1.insert(0, "Enter Lobby Name")
    e1.grid(row = 0, column = 0)

    e2 = tk.Entry(frame3)
    e2.insert(0, "Enter your name")
    e2.grid(row = 0, column = 0)

    e3 = tk.Entry(frame3)
    e3.insert(0, "Enter Lobby Code")
    e3.grid(row = 0, column = 1)

    #frame2 = tk.Frame(master)
    #frame3 = tk.Frame(master)

    #def GoBack():





    #e.grid(row = 0, column = 0, columnspan=3, pady = 10, padx = 10)
    #e.pack()



    #def callback(): 
    #   print e.get() # This is the text you may want to use later

    #b = tk.Button(master, text = "OK", width = 10)
    #b.pack()

    frame1.pack(anchor = tk.CENTER)

    tk.mainloop()

except Exception as e: 
    
    print(e)