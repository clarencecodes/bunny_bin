import socket, pickle, threading

HOST = '0.0.0.0'
PORT = 12346

TRASHBINS = {
    "blue": "Ang Mo Kio",
    "orange": "Orchard Road"
}

def clientthread(conn, addr):
    print(f"Connection from {addr} has been established")

    while True:
        try:
            message = conn.recv(16)
            if message:
                message.split()
                deserialized_message = pickle.loads(message)
                print(deserialized_message)

                if deserialized_message in TRASHBINS:
                    print(TRASHBINS[d])
                    print("Send HTTP request to twilio")
                    conn.send(message)
        except:
            continue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
while True:
    conn, addr = server.accept()
    thread = threading.Thread(clientthread(conn, addr))
    thread.start()

conn.close()
server.close()