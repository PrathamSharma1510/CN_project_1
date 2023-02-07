import socket
import os

def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', port))

    while True:
        command = input("Enter command (get/upload filename): ")
        command_parts = command.split()
        if len(command_parts) != 2:
            print("Invalid command.")
            continue

        action = command_parts[0]
        filename = command_parts[1]

        if action == "get":
            server_socket.send(command.encode('utf-8'))
            filesize = int(server_socket.recv(1024).decode())
            bytes_received = 0
            file = open(f"new{filename}", 'wb')
            chunk = server_socket.recv(1024)
            file.write(chunk)
            while bytes_received <= filesize:
                chunk = server_socket.recv(1024)
                if not chunk:
                    break
                file.write(chunk)
                bytes_received += len(chunk)
                print("bytes_received",bytes_received) 
                print("filesize",filesize)
            print('File Received')

        elif action == "upload":
            server_socket.send(command.encode('utf-8'))
            file = open(filename, 'rb')
            chunk = file.read(1024)
            server_socket.sendall(chunk)
            while(chunk):
                chunk = file.read(1024)
                server_socket.send(chunk)
            file.close()

            print("File Sent!")

        else:
            print("Invalid command.")
            server_socket.close()

        # server_socket.close()
        # print("connection closed")
        


if __name__ == "__main__":
    start=input("Enter the command and Port number :")
    start=start.split();
    if(start[0]=='ftpclient'):
        port = int(start[1])
        main(port)
    else:
        print("Not Connected")
