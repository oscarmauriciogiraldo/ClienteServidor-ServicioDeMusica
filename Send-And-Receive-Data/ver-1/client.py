import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('25.12.94.111', 5555)
#s.connect((socket.gethostname(), 5555))
s.connect(server_address)
#socket.connect("tcp://localhost:5555")
s.connect("tcp://localhost:5555")

complete_info = ''

while True:

    msg=s.recv(5555)
    if len(msg)<=0:
        break
    complete_info += msg.decode("utf-8")

print(complete_info)

"""import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5555))

while True:

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
       
        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full mensaje recivido")
            print(full_msg[HEADERSIZE:])
            new_msg = True

    print(full_msg)

""import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5555))

full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(msg.decode("utf-8"))"""