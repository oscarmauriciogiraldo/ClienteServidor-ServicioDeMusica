import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#direccion servidor
sever_address = ('25.100.99.140', 5555)
#s.bind((socket.gethostname(), 5555))#gethostname -> localhost
s.bind(sever_address)
s.listen(5)

while True:
    clientsocket, address = s.accept() 
    print(f" La Coneccion desde {address} se ha establecido!")

    clientsocket.send(bytes("binevenido al servidor!", "utf-8"))
    clientsocket.close()



"""import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5555))#gethostname -> localhost
s.listen(5)

while True:
    clientsocket, address = s.accept() 
    #print(f"Connection form {address} has been established!")
    print(f" La Coneccion desde {address} se ha establecido!")

    msg = "Bienvenido al servidor sputyfay!"
    #print(f'{len(msg):<20}' +msg) 
    msg = f'{len(msg):<{HEADERSIZE}}' + msg 


   
    clientsocket.send(bytes("binevenido al servidor!", "utf-8"))
    #clientsocket.close()


""
msg = "Bienvenido al servidor sputyfay!"
print(f'{len(msg):<20}' +msg)

#version1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5555))#gethostname -> localhost
s.listen(5)

while True:
    clientsocket, address = s.accept() 
    #print(f"Connection form {address} has been established!")

    msg = "Bienvenido al servidor sputyfay!"
    #print(f'{len(msg):<20}' +msg) 
    msg = f'{len(msg):<10}' +msg 


    print(f" La Coneccion desde {address} se ha establecido!")
    clientsocket.send(bytes("binevenido al servidor!", "utf-8"))
    clientsocket.close()
"""

 