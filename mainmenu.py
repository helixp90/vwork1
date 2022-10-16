
import tkinter as tk
from turtle import bgcolor
import sys
import subprocess
import random
import string

class GUI:

    #if __name__ == "__main__":

        def __init__(self):

            self.master = tk.Tk()

            self.master.title("Sleep Detection Monitoring Software")
            self.master.geometry("")


            self.windowtitle = tk.Label(self.master, text = "Sleep Detection Monitoring Software", font = ("Times New Roman", 15), fg = "Black")
            self.windowtitle.pack()


            self.back = tk.Button(self.master, text = "Back", bg = "Red", fg = "White", state = "disabled", command = lambda: self.goback())
            self.back.pack(anchor = tk.SW, side = tk.BOTTOM)

            self.exit = tk.Button(self.master, text = "Exit", bg = "Red", fg = "White", command = exit)
            self.exit.pack(anchor = tk.SE, side = tk.BOTTOM)


            self.masterframe = tk.Frame(self.master)

            self.masterframe.pack(anchor = tk.CENTER)


            self.clobbybutton = tk.Button(self.masterframe, text = "Create Lobby", bg = "Black", fg = "White", command = lambda: self.packcreateframe())
            self.clobbybutton.grid(row = 0, column = 0)

            self.jlobbybutton = tk.Button(self.masterframe, text = "Join Lobby", bg = "Black", fg = "White", command = lambda: self.packjoinframe())
            self.jlobbybutton.grid(row = 0, column = 1)


        def packcreateframe(self):

            self.createframe = tk.Frame(self.master)

            self.enterlname = tk.Entry(self.createframe)
            self.enterlname.insert(0, "Enter Lobby Name")
            self.enterlname.grid(row = 0, column = 0)

            self.mlobbybutton = tk.Button(self.createframe, text = "Make Lobby", bg = "Black", fg = "White", command = lambda: self.makelobby())
            self.mlobbybutton.grid(row = 1, column = 0)


            self.masterframe.pack_forget()
                    
            self.createframe.pack(anchor = tk.CENTER)
            self.back["state"] = "active"


        def packjoinframe(self):

            self.joinframe = tk.Frame(self.master)

            self.entergname = tk.Entry(self.joinframe)
            self.entergname.insert(0, "Enter your name")
            self.entergname.grid(row = 0, column = 0)

            self.enterlcode = tk.Entry(self.joinframe)
            self.enterlcode.insert(0, "Enter Lobby Code")
            self.enterlcode.grid(row = 0, column = 1)

            self.joinbutton = tk.Button(self.joinframe, text = "Join", bg = "Black", fg = "White", command = lambda: self.joinlobby())
            self.joinbutton.grid(row = 1, column = 0)


            self.masterframe.pack_forget()
                    
            self.joinframe.pack(anchor = tk.CENTER)
            self.back["state"] = "active"


        def goback(self):

            self.createframe.pack_forget() if self.createframe.winfo_ismapped() else self.joinframe.pack_forget()

            self.masterframe.pack(anchor = tk.CENTER)
            self.back["state"] = "disabled" 


        def makelobby(self):

            if (self.enterlname.index("end") == 0):

                tk.messagebox.showwarning("Lobby should have a name!")

            else:

                self.master.withdraw()
                #subprocess.call([sys.executable, "admin.py"])
                self.h = GUI2()

        def joinlobby(self):

            if (self.entergname.index("end") == 0 or self.enterlcode.index("end") == 0):

                tk.messagebox.showwarning("Fill the info!")

            else:
            
                self.master.withdraw()
                subprocess.call([sys.executable, "join.py"])

                #getvalueoflist()

    #else:

        def getvalueofclobbyname(self):

            return self.enterlname.get()

class GUI2(GUI):

    def __init__(self):

        self.master2 = tk.Toplevel()

        self.master2.title("Admin Lobby")
        self.master2.geometry("")

        self.leave = tk.Button(self.master2, text = "Leave", bg = "Red", fg = "White", command = lambda: self.leavewindow())
        self.leave.pack(anchor = tk.NW, side = tk.TOP)


        self.lnumberframe = tk.Frame(self.master2, background = "Black")
        self.lnumberframe.pack(side = tk.LEFT)

        self.lnumber = tk.Label(self.lnumberframe, text = "#" + self.makelobbycode(), font = ("Times New Roman", 15), fg = "Black")
        self.lnumber.pack(fill = "both")


        self.ecdlabel = tk.Label(self.master2, text = "Eye Closure Detection", font = ("Times New Roman", 15), fg = "Black")
        self.ecdlabel.pack(anchor = tk.CENTER)

        self.ecdpower = tk.Button(self.master2, text = "On/Off", bg = "Black", fg = "White")
        self.ecdpower.pack()


        self.bigframe = tk.Frame(self.master2, background = "Black")
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


        self.bigframe2 = tk.Frame(self.master2, background = "Black")
        self.bigframe2.pack(side = tk.RIGHT)

        self.notiframe = tk.Frame(self.bigframe2, background = "Blue")
        self.notiframe.pack(side = tk.TOP)

        self.lnotif = tk.Label(self.notiframe, text = "Sleeping Notification", font = ("Times New Roman", 15), fg = "Blue")
        self.lnotif.pack(fill = "both")


        self.notiflist = tk.Listbox(self.bigframe2)
        self.notiflist.pack(expand = 1)

    def leavewindow(self):

        self.master2.destroy()
        #subprocess.call([sys.executable, "mainmenu.py"])
        g.master.deiconify()
        #mainmenu.master.deiconify()


    def makelobbycode(self):

        self.x = random.choices(string.ascii_letters + string.digits, k = 5)

        for i in self.x:
        
            return i


if __name__ == "__main__":

    g = GUI()
    tk.mainloop()


