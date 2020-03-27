import time, socket, pickle
from gpiozero import MCP3008
import sys

TRASHBIN = 'blue'

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Invalid Command")
    print("Format: server <HOST IP> <PORT NUMBER>")
    exit()

# IP Address and Port will be based on device running server.py
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

divider = MCP3008(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP_address, Port))
while True:
    print(divider.value)
    
    if divider.value > 0.7:
        print("A lot of rubbish! Sending message to server...")
        data = pickle.dumps(TRASHBIN)

        server.send(data)

    time.sleep(1)
server.close()