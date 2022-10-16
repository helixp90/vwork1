from doctest import master
import tkinter as tk
from tkinter import messagebox
from turtle import bgcolor
import sys
import subprocess
import random
import string
from mainmenu import getvalueofclobbyname
import socket
import threading

#master = tk.Tk()

#master.title("Admin Lobby")
#master.geometry("")


class GUI2:

    def __init__(self):

        self.master2 = tk.Tk()

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
        subprocess.call([sys.executable, "mainmenu.py"])

        #mainmenu.master.deiconify()


    def makelobbycode(self):

        self.x = random.choices(string.ascii_letters + string.digits, k = 5)

        for i in self.x:
        
            return i
            

class INITSERVER(GUI2):

    def __init__(self):

        super().__init__()

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
        self.server.listen()
    
        while True:
    
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

            self.clientlist.insert("end", self.name) #append client names to listbox

            #names.append(name)
            #clients.append(conn)
    
            print(f"Name is :{self.name}")
    
            # broadcast message
            #broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
    
            self.conn.send('Connection successful!'.encode(self.FORMAT))
    
            # Start the handling thread
            self.thread = threading.Thread(target = self.handle, args = (self.conn, self.addr))
            self.thread.start()
    
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


g = GUI2()

s = INITSERVER()

tk.mainloop()

        