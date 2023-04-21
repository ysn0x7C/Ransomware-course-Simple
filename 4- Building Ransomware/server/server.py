import socket
import threading

def recvf(c):
	while True:
		data = c.recv(2048)
		if len(data) !=0:
			print(data.decode('ascii'))

def server():
	port = 4545
	ip = "127.0.0.1"
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setblocking(1)
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind((ip,port))
		s.listen(1)
		c , add = s.accept()
		print("connection from {0}:{1}".format(add[0],add[1]))
		t = threading.Thread(target=recvf,args=(c,))
		t.start()
		while True:
			command = input("command >>")
			c.send(command.encode('ascii'))
	except socket.error as e:
		print(e)
		s.close()

server()