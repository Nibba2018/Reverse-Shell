import socket
SERVER_HOST = "192.168.0.6"
SERVER_PORT = 5003
# send 1024 (1kb) a time (as buffer size)
BUFFER_SIZE = 1024
# create a socket object
s = socket.socket()

# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

# receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)

while True:
    # get the command from prompt
    command = input("Enter the command you wanna execute:")
    # send the command to the client
    s.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    results = s.recv(BUFFER_SIZE).decode()
    # print them
    print(results)
# close connection to the client
s.close()
