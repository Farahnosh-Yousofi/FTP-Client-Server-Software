import socket

def start_server():
    host = 'localhost'
    port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on port {port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connection from client {client_address} to server {server_socket}')
        
        client_socket.close()
        
if __name__ == '__main__':
    start_server()