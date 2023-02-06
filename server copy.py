import socket
def start_server(PORT, BUFFER_SIZE):
    print("Server is starting..")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", PORT)) 
    server.listen()
    print("Server started. Listening on port", PORT)
    while True:
        conn, address = server.accept()
        print("[+] New client connected: ", address)
        data =conn.recv(1024)
        command =data.decode("utf-8")
        cmd = command.split()
        
        if cmd[0] == 'get':
            file = open(cmd[1], 'rb')
            chunk =file.read (1024)
            while(chunk):
                conn.send(chunk)
                chunk = file.read(1024)
            file.close()
            print("File Sent!")
        elif cmd[0] == 'upload':
            file = open('new' +cmd[1],'wb')
            chunk = conn.recv(1024)
            while chunk:
                file.write(chunk)
                chunk = conn.recv(1024)
            file.close()
            print('File Received!')
        else :
            print('Invalid Command')
            conn.send("Invalid Command please try again!".encode("utf-8"))
            conn.closed()
            break 
        
        conn.close()

if __name__ == "__main__":
    PORT = 5108
    start_server(PORT, 1024)
