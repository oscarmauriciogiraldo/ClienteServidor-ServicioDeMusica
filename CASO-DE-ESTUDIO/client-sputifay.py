#biblioteca del sistema operativo
import os
import socket
#import threading

#IP =  socket.gethostbyname(socket.gethostname())
PORT = 5555
#ADDR = (IP, PORT)
ADDR = ('localhost', PORT)
SIZE = 1024
FORMAT = "utf-8"
#SERVER_DATA_PATH = "server-data"
SERVER_DATA_PATH = "client-data"

def main():
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(ADDR)

    while True:
        data = socket_client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "OK":
            print(f"{msg}")
        elif cmd == "DESCONECTADO":
            print(f"{msg}")
            break

        # data-message
        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "MENU":
            socket_client.send(cmd.encode(FORMAT))

        elif cmd == "LOGOUT":
            socket_client.send(cmd.encode(FORMAT))
            break

        elif cmd == "PLAYLIST":
            socket_client.send(cmd.encode(FORMAT))

        ####################################################################################
        ##################################################################################
        ## upload 
        ## para descargar 
        elif cmd == "UPLOAD":

            ################################################################
            ## UPLOAD@Filename@text

            """#"""
            path = data[1]
            with open(f"{path}", "r") as f:
                text = f.read()

            ## [client_data, data.txt]
            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            socket_client.send(send_data.encode(FORMAT))
            #socket_client.recv(send_data.encode(FORMAT))
            ## upload 
            ################################################################
            """ ############## intento fallido ############# """
            """
            name = data[1]
            text = data[2]

            filepath = os.path.join(SERVER_DATA_PATH, name)
            with open(filepath, "w") as f:
                f.write(text)"""
        ####################################################################################
        ##################################################################################

        elif cmd == "BORRAR":
            socket_client.send(f"{cmd}@{data[1]}".encode(FORMAT))

    
    print("Desconectado del servidor")
    socket_client.close()

if __name__ == "__main__":
    main()