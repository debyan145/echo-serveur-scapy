#!/usr/bin/python3
import socket
import sys



def echo():
    s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
    port=7777
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("",port))
    s.listen(1)
    while True:
        try:
            client_socket,client_address=s.accept()
            print(f"Connection accepté par le serveur")
        except Exception as e:
            print("Erreur dans l'acceptation")
            sys.exit(1)
        while True:
            try:
                data=client_socket.recv(1500)
            except Exception as e:
                print("Erreur dans la reception des paquets")
                sys.exit(1)
            if not data:
                print("Aucune donnée reçu")
                break
            print(data.decode())

        client_socket.close()
        print("Connection terminée")


            
        
echo()
