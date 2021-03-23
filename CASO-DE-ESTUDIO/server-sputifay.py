#biblioteca del sistema operativo
import os
import socket
import threading

#IP =  socket.gethostbyname(socket.gethostname())
PORT = 5555
#server address
#ADDR = (IP, PORT)
ADDR = ('localhost', PORT)
SIZE = 1024
FORMAT = "utf-8"
#SERVER_DATA_PATH = "server-data"
SERVER_DATA_PATH = "client-data"

#RECEPTOR DE SOLICITUDES 
def handle_client(connexion, addres):
    print(f"[Nueva Conexion] {addres} Conectado con Sputifay.")
    connexion.send("OK@Bienvenido a sputifay server".encode(FORMAT))

    while True:
        data = connexion.recv(SIZE).decode(FORMAT)
        #data = connexion.send(SIZE).decode(FORMAT)
        ##print(data)
        data = data.split("@")
        ##print(data)
        cmd_message = data[0]
        #print(cmd)

        if cmd_message == "MENU":
            send_data = "OK@"
            send_data += "PLAYLIST: LISTA DE CANCIONES .\n"

            connexion.send(send_data.encode(FORMAT))

        elif cmd_message == "LOGOUT":
            break

        elif cmd_message == "PLAYLIST":
            #pass
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"

            if len(files) == 0:
                send_data += "no hay lista de reproduccion en el momento"
            else:
                send_data += "\n".join(f for f in files)
            connexion.send(send_data.encode(FORMAT))
        

        ####################################################################################
        ##################################################################################
        elif cmd_message == "UPLOAD":
            #pass
            # recibe el archivo
            ################################################################
            """"""
            name = data[1]
            text = data[2]

            filepath = os.path.join(SERVER_DATA_PATH, name)
            with open(filepath, "w") as f:
                f.write(text)
            
            # recibe el archivo
            
            """ ##############intento faccido##########################"""
            """
            path = data[1]
            with open(f"{path}", "r") as f:
                text = f.read()

            ## [client_data, data.txt]
            filename = path.split("/")[-1]
            #send_data = f"{cmd}@{filename}@{text}"
            send_data = f"{cmd_message}@{filename}@{text}"
            #socket_server.send(send_data.encode(FORMAT))
            connexion.send(send_data.encode(FORMAT))"""
            ################################################################

            send_data = "OK@Descarga Completa."
            connexion.send(send_data.encode(FORMAT))
        ####################################################################################
        ##################################################################################

        elif cmd_message == "DELETE":
            #pass
            files = os.listdir(SERVER_DATA_PATH)
            send_data ="OK@"
            filename = data[1]

            if len(files) == 0:
                send_data += "NO HAY ARCHIVOS PARA ELEMINAR"
            else:
                if filename in files:
                    os.system(f"rm {SERVER_DATA_PATH}/{filename}")
                    send_data += "Archivo Borrado."
                else:
                    send_data += " Archivo No Encontrado"
            connexion.send(send_data.encode(FORMAT))

        elif cmd_message == "Descargar":
            pass
             ## UPLOAD@Filename@text
            """
            path = data[1]
            with open(f"{path}", "r") as f:
                text = f.read()

            ## [client_data, data.txt]
            filename = path.split("/")[-1]
            send_data = f"{cmd_message}@{filename}@{text}"
            socket_server.send(send_data.encode(FORMAT))"""
            """"""
            
            

    print(f"[DESCONECTADO] {addres} desconectado")
            


def main():
    print("[INICIANDO] El servidor esta Iniciando")
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(ADDR)
    socket_server.listen()
    print("[ESCUCHANDO] El servidor esta Escuchando El Puerto")

    while True:
        connexion, addres = socket_server.accept()
        thread = threading.Thread(target=handle_client, args=(connexion, addres))
        thread.start()


if __name__ == "__main__":
    main()
