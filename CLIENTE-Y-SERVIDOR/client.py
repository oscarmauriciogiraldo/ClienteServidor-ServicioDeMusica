"""
Created on Thu Feb 11 16:07:18 2021

@author: Oscar M Giraldo H
"""

import zmq

######bloque para crear el socket#############

#creo un contexto
context = zmq.Context()
#creo el socket, REQ: a travez de este socket se realizan solicitudes 
socket = context.socket(zmq.REQ)
""" se asocia el socket para interactuar con el agente 
    que escucha el pueto 5555 de localhost
    
    todo esto corre de manera local"""
socket.connect("tcp://localhost:5555")
#######bloque para crear el socket ##############

for i in range(10):
    s = "hola {}".format(i)
    socket.send(s.encode('utf-8'))
    m = socket.recv()
    print(m)