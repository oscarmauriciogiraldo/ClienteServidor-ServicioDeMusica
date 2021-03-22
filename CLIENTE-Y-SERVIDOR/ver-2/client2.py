#import socket
import zmq
import json

context = zmq.Context()
#socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client = context.socket(zmq.REQ)
print("conexion establecida con el servidor")
#socket_client.connect(('localhost', 5555))
socket_client.connect("tcp://localhost:5555")
print("conectada con el servidor")

a = 10
b = 20
message = [str(a).encode('utf-8'), str(b).encode('utf-8')]
socket_client.send_mutipart(message)
message = socket_client.recv()
print(message)