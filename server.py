# import socket library
import socket
 
# import threading library
import threading

import multiprocessing

from multiprocessing import Process
 
# Choose a port that is free
class INITSERVER(): #initializes and runs the server

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

        self.startChat(self)

        #self.process = Process(target = self.startChat, args = (self,))

        #self.process.start()
        
        # function to start the connection 

    def startChat(self):
       
        print("server is working on " + self.SERVER)
    
        # listening for connections
        self.server.listen(30)

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

            #names.append(name)
            #clients.append(conn)

            #self.clientlist.insert("end", self.name) #append client names to listbox

            print(f"Name is {self.name}")

            self.returnvalue(self.name)

            # broadcast message
            #broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))

            #self.conn.send('Connection successful!'.encode(self.FORMAT))

            # Start the handling thread
            #self.thread = threading.Thread(target = self.handle, args = (self.conn, self.addr))
            #self.thread.start()

            # no. of clients connected
            # to the server
            #print(f"active connections {threading.activeCount()-1}")

        
    def returnvalue(x):

        return x
        
    # method to handle the
    # incoming messages
    
    
    def handle(self, conn, addr): #unused code
    
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
    
    
    def broadcastMessage(self, message): #unused code
        
        for client in self.clients:
            
            client.send(message)   