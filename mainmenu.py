
from multiprocessing.dummy import Process, active_children
import tkinter as tk
from turtle import bgcolor
import sys
import subprocess
import random
import string
import socket
import threading
from tkinter import messagebox
from tkinter import ttk
from threading import Thread
from threading import Event
from multiprocessing import Process

lobbycode = ''


class GUI:  #mainmenu window

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

            self.current_frame = self.createframe


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

            self.current_frame = self.joinframe


        def goback(self):

            #self.createframe.pack_forget() if self.createframe.winfo_ismapped() else self.joinframe.pack_forget()

            self.current_frame.pack_forget()

            self.masterframe.pack(anchor = tk.CENTER)
            self.back["state"] = "disabled" 


        def makelobby(self): #hides main menu window and initializes host GUI

            global clobbyname

            if (self.enterlname.index("end") == 0):

                messagebox.showwarning("Invalid input!", "Lobby should have a name!")

            else:

                clobbyname = self.enterlname.get()

                self.master.withdraw()
                #subprocess.call([sys.executable, "admin.py"])
                self.h = GUI2()
                

        def joinlobby(self):

            if (self.entergname.index("end") == 0 or self.enterlcode.index("end") == 0):

                messagebox.showwarning("Invalid input!", "Name and/or code should have input!")

            else:
                
                try:
                    
                    #if self.enterlcode.get() == lobbycode:

                        self.master.withdraw()
                        #subprocess.call([sys.executable, "join.py"])
                        self.j = GUI3()

                        #getvalueoflist()

                except Exception as e:

                    messagebox.showerror("Server down!", "The server you're trying to connect to may be inactive.")

                    print (e)

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

        self.lnumber = tk.Label(self.lnumberframe, font = ("Times New Roman", 15), fg = "Black")
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

        self.makelobbycode()

        #self.event = threading.Event()

        self.s = INITSERVER()
        
        self.process = Process(target = self.s.startChat)

        self.process.start()
        #self.thread.join()
        
        

    def leavewindow(self):

        self.process.terminate()

        self.process.join()
        
        self.process.close()

        print("Process closed")

        self.s.server.close()

        self.master2.destroy()
        
        #subprocess.call([sys.executable, "mainmenu.py"])
        g.master.deiconify()
        #mainmenu.master.deiconify()


    def makelobbycode(self):

        global lobbycode

        lobbycode = random.choices(string.ascii_letters + string.digits, k = 5)

        lobbycode = [str(x) for x in lobbycode]

        self.msg = ''.join(lobbycode)

        messagebox.showinfo("New Lobby Code!", "Your lobby code is: " + self.msg)

        self.lnumber.config(text = self.msg)


class INITSERVER(GUI2):

    def __init__(self):

        #threading.Thread.__init__(self)

        #super().__init__()

        #self.event = event
        
        # Choose a port that is free
        self.PORT = 5000
        
        # An IPv4 address is obtained
        # for the server.
        self.SERVER = socket.gethostbyname(socket.gethostname())
        
        # Address is stored as a tuple
        self.ADDRESS = (self.SERVER, self.PORT)
        
        # the format in which encoding
        # and decoding will occur
        self.FORMAT = "utf-8"
        
        # Lists that will contains
        # all the clients connected to
        # the server and their names.
        self.clients, self.names = [], []
        
        # Create a new socket for
        # the server
        self.server = socket.socket(socket.AF_INET,
                            socket.SOCK_STREAM)
        
        # bind the address of the
        # server to the socket
        self.server.bind(self.ADDRESS)
        
        # function to start the connection 

    def startChat(self):

        print("server is working on " + self.SERVER)
    
        # listening for connections
        self.server.listen(30)

        while True:
            
            #clientlist = self.clientlist

            # accept connections and returns
            # a new connection to the client
            #  and  the address bound to it
            self.conn, self.addr = self.server.accept()
            #self.conn.send("NAME".encode(FORMAT))

            # 1024 represents the max amount
            # of data that can be received (bytes)
            self.name = self.conn.recv(1024).decode(self.FORMAT)

            # append the name and client
            # to the respective list

            #names.append(name)
            #clients.append(conn)

            self.clientlist.insert("end", self.name) #append client names to listbox

            

            print(f"Name is :{self.name}")

            # broadcast message
            #broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))

            self.conn.send('Connection successful!'.encode(self.FORMAT))

            # Start the handling thread
            #self.thread = threading.Thread(target = self.handle, args = (self.conn, self.addr))
            #self.thread.start()

            # no. of clients connected
            # to the server
            print(f"active connections {threading.activeCount()-1}")

    # method to handle the
    # incoming messages
    
    
    def handle(self, conn, addr):
    
        print(f"new connection {addr}")
        connected = True
    
        while connected:
            # receive message
            self.message = conn.recv(1024)
    
            # broadcast message
            self.broadcastMessage(self.message)
    
        # close the connection
        conn.close()
    
    # method for broadcasting
    # messages to the each clients
    
    
    def broadcastMessage(self, message):
        
        for client in self.clients:
            
            client.send(message)   


class GUI3(GUI):

    def __init__(self):

        self.master3 = tk.Toplevel()

        self.master3.title("Joined Lobby")
        self.master3.geometry("")

        self.leave = tk.Button(self.master3, text = "Leave", bg = "Red", fg = "White", command = lambda: self.leavewindow())
        self.leave.pack(anchor = tk.NW, side = tk.TOP)


        self.lnameframe = tk.Frame(self.master3, background = "Black")
        self.lnameframe.pack(side = tk.TOP)

        self.lname = tk.Label(self.lnameframe, text = "+", font = ("Times New Roman", 15), fg = "Black")
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

        self.i = INITCLIENT()

    def leavewindow(self):

        self.i.client.close()

        self.master3.destroy()

        g.master.deiconify()
        #subprocess.call([sys.executable, "mainmenu.py"])

        #mainmenu.master.deiconify()

class INITCLIENT(GUI3):

    def __init__(self):

        self.PORT = 5000
        self.SERVER = "192.168.0.19"
        self.ADDRESS = (self.SERVER, self.PORT)
        self.FORMAT = "utf-8"

        self.client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

        self.client.connect(self.ADDRESS)

        self.name = g.entergname.get()

        self.client.send(self.name.encode(self.FORMAT))





if __name__ == "__main__":

    #event = threading.Event()

    g = GUI()
    tk.mainloop()


