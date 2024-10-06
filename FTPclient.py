import socket

host = 'localhost'
port = 8080
 
def get_file_from_server(filename):
    
    try:
        
        # Create a socket to connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print('Connected to server')
    
        # Send "get <filename>" command to the server
        client_socket.sendall(f'G {filename}'.encode())
    
        # Receive the file from the server
        new_Filename = "new" + filename
        with open(new_Filename, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f'File: {new_Filename} downloaded successfully')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        if client_socket:
            client_socket.close()
       
if __name__ == '__main__':
    while True:
        print("Enter 'get <filename>' to download or 'upload <filename>' to upload or 'exit' to quit.")
        command = input("ftp> ")
        if command.startswith("get "):
            filename = command.split(" ")[1]
            get_file_from_server(filename)