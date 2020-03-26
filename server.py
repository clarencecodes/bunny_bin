import socket, pickle, threading
from twilio.rest import Client

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
                    print("Sending HTTP request to Twilio...")
                    triggerSMSToCleaner(TRASHBINS[deserialized_message], '+65')

        except:
            continue

def triggerSMSToCleaner(dustbin_location, mobile_number):
    account_sid = 'redacted'
    auth_token = 'redacted'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Trash bin at {dustbin_location} is full! Please empty me!",
        from_='Bunny Bin',
        to=mobile_number
    )

    print(message.sid)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
while True:
    conn, addr = server.accept()
    thread = threading.Thread(clientthread(conn, addr))
    thread.start()

conn.close()
server.close()