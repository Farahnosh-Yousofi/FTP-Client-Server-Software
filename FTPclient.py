import socket

def connect():
    host = 'localhost'
    port = 8080
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print('Connected to server')
    
if __name__ == '__main__':
    connect()