# Conexxion Cliente y Servidor 
  
  Arquitectura Cliente y Servidor
# Send and Receive Data 
# Enviar y recibir archivos en Python 

## Hilos y multihilos 
 ### Procesos y Multiprocesos

Esta arquitectura Cliente/Servidor esta basada en la transferencia de archivos multiprocesos

  #### server
  while True:
    clientsocket, address = s.accept() 
    #print(f"Connection form {address} has been established!")
    print(f" La Coneccion desde {address} se ha establecido!")
    clientsocket.send(bytes("binevenido al servidor!", "utf-8"))
    clientsocket.close()

  #### client
  full_msg = ''
  while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(msg.decode("utf-8"))