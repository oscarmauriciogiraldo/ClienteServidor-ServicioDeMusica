import socket
import pickle

a=10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5555))#gethostname -> localhost
s.listen(5)

while True:
    clientsocket, address = s.accept() 
    print(f" La Coneccion desde {address} se ha establecido!")

    m= {1:"Client", 2:"Server"}
    mymsg = pickle.dumps(m)
    mymsg = bytes(f'{len(mymsg):<{a}}', "utf-8") + mymsg
    clientsocket.send(mymsg)
    """
    clientsocket.send(bytes("binevenido al servidor!", "utf-8"))
    clientsocket.close()
    """