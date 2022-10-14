
import tkinter as tk
from turtle import bgcolor
import sys
import subprocess



class GUI:

    if __name__ == "__main__":

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
        self.entergname(0, "Enter your name")
        self.entergname(row = 0, column = 0)

        self.enterlcode = tk.Entry(self.joinframe)
        self.enterlcode(0, "Enter Lobby Code")
        self.enterlcode(row = 0, column = 1)

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
            subprocess.call([sys.executable, "admin.py"])

    def joinlobby(self):

        if (self.entergname.index("end") == 0 or self.enterlcode.index("end") == 0):

            tk.messagebox.showwarning("Fill the info!")

        else:
         
            self.master.withdraw()
            subprocess.call([sys.executable, "join.py"])

            #getvalueoflist()

    def getvalueofclobbyname(self):

        return self.enterlname.get()




g = GUI()

tk.mainloop()

