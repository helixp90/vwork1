from doctest import master
import tkinter as tk
from turtle import bgcolor

from . import mainmenu

#import mainmenu

#master = tk.Tk()

#master.title("Admin Lobby")
#master.geometry("")


class GUI:

    def __init__(self):

        self.master = tk.Tk()

        self.master.title("Joined Lobby")
        self.master.geometry("")

        self.leave = tk.Button(self.master, text = "Leave", bg = "Red", fg = "White", command = exit)
        self.leave.pack(anchor = tk.NW, side = tk.TOP)


        self.lnameframe = tk.Frame(self.master, background = "Black")
        self.lnameframe.pack(side = tk.TOP)

        self.lname = tk.Label(self.lnameframe, text = "Ma'am Jenith's Lobby", font = ("Times New Roman", 15), fg = "Black")
        self.lname.pack(fill = "both")


        self.ecdlabel = tk.Label(self.master, text = "Sleeping Detection Status", font = ("Times New Roman", 15), fg = "Black")
        self.ecdlabel.pack(anchor = tk.CENTER)


        self.bigframe = tk.Frame(self.master, background = "Black")
        self.bigframe.pack(anchor = tk.CENTER)

        self.lname = tk.Label(self.bigframe, text = "Watching you", font = ("Times New Roman", 15), fg = "Blue")
        self.lname.pack(fill = "both")


        self.bigframe2 = tk.Frame(self.master, background = "Black")
        self.bigframe2.pack(side = tk.RIGHT)

        self.notiframe = tk.Frame(self.bigframe2, background = "Blue")
        self.notiframe.pack(side = tk.TOP)

        self.lnotif = tk.Label(self.notiframe, text = "Sleeping Notification", font = ("Times New Roman", 15), fg = "Blue")
        self.lnotif.pack(fill = "both")


        self.notiflist = tk.Listbox(self.bigframe2)
        self.notiflist.pack(expand = 1)

        


g = GUI()

tk.mainloop()

        