#!/usr/bin/python
import socket
import paramiko
import threading

class SSHServer(paramiko.ServerInterface):

    def check_auth_password(self, username: str, password: str) -> int:
        client_ip = client_sock.getpeername()[0]
        print(f"Connection from {client_ip} - {username}:{password}")
        #print(f"{username}:{password}")
        return paramiko.AUTH_FAILED

def handle_connection(client_sock):
    transport = paramiko.Transport(client_sock)
    server_key= paramiko.RSAKey.from_private_key_file('key')
    transport.add_server_key(server_key)
    ssh = SSHServer()
    transport.start_server(server=ssh)

def main():
    print("Iniciando dummy SSH server como honeypot 🍯")
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('', 2222))
    server_sock.listen(223)

    while True:
        client_sock, client_addr = server_sock.accept()
        print(f"Connection from {client_addr[0]}:{client_addr[1]}")
        t = threading.Thread(target=handle_connection, args=(client_sock,))
        t.start()
        
    ## prueba
    

if __name__ == "__main__":
    main()
 