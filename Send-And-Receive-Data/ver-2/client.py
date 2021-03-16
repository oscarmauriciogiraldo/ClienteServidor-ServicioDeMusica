import socket
import pickle

a=10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5555))

#complete_info = ''

while True:
    complete_info = b''
    receive_msg = True
    while True:
        mymsg = s.recv(16)
        if receive_msg:
            print(f"la longitud del mensaje es = {mymsg[:a]}")
            x = int(mymsg[:a])
            receive_msg = False
        complete_info += mymsg

        if len(complete_info) -a == x:
            print(" recibiendo la informacion completa")
            print(complete_info[a:])
            m = pickle.loads(complete_info[a:])
            print(m)
            receive_msg = True
            complete_info = b''
    print(complete_info)

"""
while True:

    msg=s.recv(5555)
    if len(msg)<=0:
        break
    complete_info += msg.decode("utf-8")

print(complete_info)"""