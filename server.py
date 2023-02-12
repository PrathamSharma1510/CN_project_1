import socket
def start_server(port, BUFFER_SIZE):
    print("Server is starting..")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", port)) 
    server.listen()
    print("Server started. Listening on port", port)
    while True:
        conn, add = server.accept()
        print("[+] New client connected: ", add)
        data =conn.recv(1024)
        command =data.decode("utf-8")
        data_split = command.split()
        
        if data_split[0] == 'get':
            file = open(data_split[1], 'rb')
            file_chunks =file.read (1024)
            while(file_chunks):
                conn.send(file_chunks)
                file_chunks = file.read(1024)
            file.close()
            print("File Sent!")
        elif data_split[0] == 'upload':
            file = open('new' +data_split[1],'wb')
            file_chunks = conn.recv(1024)
            while file_chunks:
                file.write(file_chunks)
                file_chunks = conn.recv(1024)
            file.close()
            print('File Received!')
        else :
            print('Invalid Command')
            conn.send("Invalid Command please try again!".encode("utf-8"))
            conn.closed()
            break 
        
        conn.close()

if __name__ == "__main__":
    port = 5108
    start_server(port, 1024)
