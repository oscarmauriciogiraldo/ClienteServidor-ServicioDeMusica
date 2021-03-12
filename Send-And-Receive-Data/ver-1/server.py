import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))#gethostname -> localhost
s.listen(5)

while True:
    clientsocket, address = s.accept() 
    #print(f"Connection form {address} has been established!")
    print(f"Coneccion desde {address} se ha establecido!")
    clientsocket.send(bytes("binevenido al servidor!", "utf-8"))

 