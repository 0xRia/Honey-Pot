import paramiko
import socket
import threading
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

class HoneypotSSHServer(paramiko.ServerInterface):
    def __init__(self, client_ip):
        self.client_ip = client_ip

    def check_auth_password(self, username, password):
        logging.info(f"SSH Auth Attempt from {self.client_ip}: Username: {username}, Password: {password}")
        return paramiko.AUTH_SUCCESSFUL

    def check_auth_publickey(self, username, key):
        logging.info(f"SSH Public Key Auth Attempt from {self.client_ip}: Username: {username}")
        return paramiko.AUTH_SUCCESSFUL

    def get_allowed_auths(self, username):
        return 'password,publickey'

def handle_client(client_sock, client_addr):
    client_ip = client_addr[0]
    transport = paramiko.Transport(client_sock)
    transport.add_server_key(paramiko.RSAKey.generate(2048))  # Generate a key for the server
    server = HoneypotSSHServer(client_ip)
    try:
        transport.start_server(server=server)
        channel = transport.accept(20)
        if channel:
            channel.close()
    except Exception as e:
        logging.error(f"SSH Error from {client_ip}: {str(e)}")
    finally:
        transport.close()

def start_ssh_honeypot():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('0.0.0.0', 22))
    server_sock.listen(100)
    logging.info("SSH Honeypot started on port 22")

    while True:
        client_sock, client_addr = server_sock.accept()
        logging.info(f"SSH Connection from {client_addr[0]}:{client_addr[1]}")
        t = threading.Thread(target=handle_client, args=(client_sock, client_addr))
        t.start()

if __name__ == '__main__':
    start_ssh_honeypot()
