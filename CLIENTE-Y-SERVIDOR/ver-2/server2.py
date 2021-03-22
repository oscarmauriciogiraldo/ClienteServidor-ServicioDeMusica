#import socket
import zmq
import json

context = zmq.Context()
#socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server = context.socket(zmq.REP)
#socket_server.bind(('localhost', 5555))
socket_server.bind("tcp://*:5555")

#socket_server.listen(3)
#print("Conexion Establecida.")
print("Conexion Establecida con el servidor.")

"""
conexion_socket, direccion = socket_server.accept()
print("Primera Conexxion : ", direccion[0])"""

print("esperando peticion")

data = socket.recv(1024)
file = open