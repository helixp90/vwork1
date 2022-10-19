from doctest import master
import tkinter as tk
from turtle import bgcolor
import sys
import subprocess
import mainmenu

#import mainmenu

#master = tk.Tk()

#master.title("Admin Lobby")
#master.geometry("")


class GUI3:

    def __init__(self):

        self.master3 = tk.Tk()

        self.master3.title("Joined Lobby")
        self.master3.geometry("")

        self.leave = tk.Button(self.master3, text = "Leave", bg = "Red", fg = "White", command = lambda: self.leavewindow())
        self.leave.pack(anchor = tk.NW, side = tk.TOP)


        self.lnameframe = tk.Frame(self.master3, background = "Black")
        self.lnameframe.pack(side = tk.TOP)

        self.lname = tk.Label(self.lnameframe, text = mainmenu.getvalueoflist(), font = ("Times New Roman", 15), fg = "Black")
        self.lname.pack(fill = "both")


        self.ecdlabel = tk.Label(self.master3, text = "Sleeping Detection Status", font = ("Times New Roman", 15), fg = "Black")
        self.ecdlabel.pack(anchor = tk.CENTER)


        self.bigframe = tk.Frame(self.master3, background = "Black")
        self.bigframe.pack(anchor = tk.CENTER)

        self.lname = tk.Label(self.bigframe, text = "Watching you", font = ("Times New Roman", 15), fg = "Blue")
        self.lname.pack(fill = "both")


        self.bigframe2 = tk.Frame(self.master3, background = "Black")
        self.bigframe2.pack(side = tk.RIGHT)

        self.notiframe = tk.Frame(self.bigframe2, background = "Blue")
        self.notiframe.pack(side = tk.TOP)

        self.lnotif = tk.Label(self.notiframe, text = "Sleeping Notification", font = ("Times New Roman", 15), fg = "Blue")
        self.lnotif.pack(fill = "both")


        self.notiflist = tk.Listbox(self.bigframe2)
        self.notiflist.pack(expand = 1)

    def leavewindow(self):

        self.master3.destroy()
        #subprocess.call([sys.executable, "mainmenu.py"])

        #mainmenu.master.deiconify()

        


g = GUI3()

tk.mainloop()

        