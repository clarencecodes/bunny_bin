import time, socket, pickle
from gpiozero import MCP3008

HOST = '172.20.10.13' # IP Address of device running server.py
PORT = 12346

TRASHBIN = 'blue'

divider = MCP3008(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
while True:
    print(divider.value)
    
    if divider.value > 0.7:
        print("A lot of rubbish! Sending message to server...")
        data = pickle.dumps(TRASHBIN)

        server.send(data)

    time.sleep(1)
server.close()