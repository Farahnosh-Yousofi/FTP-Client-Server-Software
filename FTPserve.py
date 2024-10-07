import socket

def send_file_to_client(client_socket, filename):
    try:
        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                     break
                client_socket.sendall(data)
        print(f'File: {filename} sent successfully')
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        client_socket.sendall(b'Error: File {filename} not found')
            

def receive_file_from_client(client_socket, filename):
    new_filename = "new" + filename
    with open(new_filename, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
    print(f"File '{new_filename}' received successfully.")



def start_server():
    host = 'localhost'
    port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on port {port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connection from client {client_address}')
        
        command = client_socket.recv(1024).decode()
        if command.startswith('get '):
            filename = command.split(' ')[1]
            send_file_to_client(client_socket, filename)
        elif command.startswith('upload '):
            filename = command.split(' ')[1]
            receive_file_from_client(client_socket, filename)
        client_socket.close()
        
if __name__ == '__main__':
    start_server()