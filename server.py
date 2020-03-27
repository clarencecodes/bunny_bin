import socket, pickle, threading
from twilio.rest import Client

HOST = '0.0.0.0'
PORT = 12345

class TrashBin:
    def __init__(self, color_code, location):
        self.color_code = color_code
        self.location = location
        self.bin_full_request_count = 0

blue = TrashBin("blue", "Ang Mo Kio")
orange = TrashBin("orange", "Orchard Road")

TRASH_BINS = {
    "blue": blue,
    "orange": orange
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

                if deserialized_message in TRASH_BINS:
                    color_code = deserialized_message

                    # To ensure that the infrared sensor isn't being tampered with, only trigger the SMS when we know
                    # that the trash bin is really full, and only after multiple (10) requests from the client
                    if TRASH_BINS[color_code].bin_full_request_count is 10:
                        print(f"Sending SMS to cleaner and resetting {color_code} bin full request count")
                        triggerSMSToCleaner(TRASH_BINS[color_code].location, '+65redacted')
                        TRASH_BINS[color_code].bin_full_request_count = 0
                    else:
                        TRASH_BINS[color_code].bin_full_request_count += 1
                        print(f"Incremented {color_code} bin full request count to {TRASH_BINS[color_code].bin_full_request_count}")

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