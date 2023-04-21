import socket
import time
def client():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("127.0.0.1",4545))
        s.send(b'hello world server')
        s.close()
        print("done")
    except ConnectionRefusedError as e:
        print(e)
        print("try to connect again with the server with in 2 min")
        time.sleep(2 * 60)
        client()
client()
