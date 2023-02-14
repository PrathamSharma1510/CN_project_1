import socket


def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', port))
    flag = False

    while True:
        if(flag):
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect(('localhost', port))
            flag = False
        print("Enter command ('exit') to stop server and client")
        command = input("Enter command (get/upload filename): ")
        command_parts = command.split()
        if command_parts[0] == "get":
            try :
                file = open(command_parts[1], 'rb')
            except :
                print("File was not found please check the name")
                flag = True
            else:
                server_socket.send(command.encode('utf-8'))
                file = open(f"new{command_parts[1]}", 'wb')
                file_chunks = server_socket.recv(1024)
                while file_chunks:
                    file.write(file_chunks)
                    file_chunks = server_socket.recv(1024)
                file.close()
                print('File Received')
                flag = True

        elif command_parts[0] == "upload":
            try:
                file = open(command_parts[1], 'rb')
            except:
                print("File was not found please check the name")
                flag = True
            else:
                server_socket.send(command.encode('utf-8'))
                file_chunks = file.read(1024)
                server_socket.send(file_chunks)
                while(file_chunks):
                    file_chunks = file.read(1024)
                    server_socket.send(file_chunks)
                file.close()

                print("File Sent!")
                flag = True

        elif command == "exit":
            server_socket.send(command.encode('utf-8'))
            print("The connection is exited")
            server_socket.close()
            break
        else:
            print("Invalid command Enter a valid command")
            server_socket.close()
            flag = True
            # break
        server_socket.close()


if __name__ == "__main__":
    try:
        start = input("Enter the command and port number :")
        start = start.split()
        if(start[0] == 'ftpclient'):
            port = int(start[1])
            main(port)
        else:
            print("Command is not proper")
    except:
        print("No Server connected on that Port")
