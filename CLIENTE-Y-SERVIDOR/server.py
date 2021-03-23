"""
Created on Thu Feb 11 16:07:18 2021

@author: Oscar M Giraldo H
"""

import zmq
""" Canal de comunicacion desde el lado del servidor """

#creo un contexto
context = zmq.Context()
#creo el socket, REP: Responde a solicitudes 
socket = context.socket(zmq.REP)
#se asocia el socket con el puerto 5555 de la interfaz de red por defecto
# "*" usa la interfaz por defecto con el protocolo  tcp
socket.bind("tcp://25.100.99.140:5555")

print("antes de comenzar a atender")
while True:
    print("esperando mensaje")
    m = socket.recv()
    print("atendiendo mensaje")
    print(m)
    socket.send(b'ok')