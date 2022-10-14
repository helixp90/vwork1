from doctest import master
import tkinter as tk
from tkinter import messagebox
from turtle import bgcolor
import sys
import subprocess
import random
import string
import mainmenu

#master = tk.Tk()

#master.title("Admin Lobby")
#master.geometry("")


class GUI:

    def __init__(self):

        self.master = tk.Tk()

        self.master.title("Admin Lobby")
        self.master.geometry("")

        self.leave = tk.Button(self.master, text = "Leave", bg = "Red", fg = "White", command = lambda: self.leavewindow())
        self.leave.pack(anchor = tk.NW, side = tk.TOP)


        self.lnumberframe = tk.Frame(self.master, background = "Black")
        self.lnumberframe.pack(side = tk.LEFT)

        self.lnumber = tk.Label(self.lnumberframe, text = "#" + self.makelobbycode(), font = ("Times New Roman", 15), fg = "Black")
        self.lnumber.pack(fill = "both")


        self.ecdlabel = tk.Label(self.master, text = "Eye Closure Detection", font = ("Times New Roman", 15), fg = "Black")
        self.ecdlabel.pack(anchor = tk.CENTER)

        self.ecdpower = tk.Button(self.master, text = "On/Off", bg = "Black", fg = "White")
        self.ecdpower.pack()


        self.bigframe = tk.Frame(self.master, background = "Black")
        self.bigframe.pack(anchor = tk.CENTER)

        
        self.nameframe = tk.Frame(self.bigframe, background = "Blue")
        self.nameframe.pack(anchor = tk.NW, side = tk.LEFT)

        self.lname = tk.Label(self.nameframe, text = "Name", font = ("Times New Roman", 15), fg = "Blue")
        self.lname.pack(fill = "both")

        self.statusframe = tk.Frame(self.bigframe, background = "Blue")
        self.statusframe.pack(anchor = tk.CENTER, side = tk.TOP)

        self.lstatus = tk.Label(self.bigframe, text = "Status", font = ("Times New Roman", 15), fg = "Blue")
        self.lstatus.pack(fill = "both")

        self.idframe = tk.Frame(self.bigframe, background = "Blue")
        self.idframe.pack(anchor = tk.NE, side = tk.RIGHT)

        self.lid = tk.Label(self.idframe, text = "#ID Number", font = ("Times New Roman", 15), fg = "Blue")
        self.lid.pack(fill = "both")


        self.clientframe = tk.Frame(self.bigframe, background = "Green")
        self.clientframe.pack(side = tk.BOTTOM)


        self.clientlist = tk.Listbox(self.clientframe)
        self.clientlist.pack(expand = 1)


        self.bigframe2 = tk.Frame(self.master, background = "Black")
        self.bigframe2.pack(side = tk.RIGHT)

        self.notiframe = tk.Frame(self.bigframe2, background = "Blue")
        self.notiframe.pack(side = tk.TOP)

        self.lnotif = tk.Label(self.notiframe, text = "Sleeping Notification", font = ("Times New Roman", 15), fg = "Blue")
        self.lnotif.pack(fill = "both")


        self.notiflist = tk.Listbox(self.bigframe2)
        self.notiflist.pack(expand = 1)

    def leavewindow(self):

        self.master.destroy()
        subprocess.call([sys.executable, "mainmenu.py"])

        #mainmenu.master.deiconify()


    def makelobbycode(self):

        self.x = random.choices(string.ascii_letters + string.digits, k = 5)

        for i in self.x:
        
            return i
            

        


g = GUI()

tk.mainloop()

        