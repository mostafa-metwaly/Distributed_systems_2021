import socket
import sys
import threading



class Server:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections = []

	def __init__(self):
		self.sock.bind(('0.0.0.0', 8989))
		self.sock.listen(5)

	def handler(self, c, a):
		while True:
			data = c.recv(1024)
			for connection in self.connections:
				connection.send(data)

			if not data:
				print(str(a[0]) + ':' + str(a[1]), "disconnected")
				self.connections.remove(c)
				c.close()
				break

	def run(self):
		while True:
			c, a = self.sock.accept()
			cThread = threading.Thread(target=self.handler, args=(c, a))
			cThread.daemon = True
			cThread.start()
			self.connections.append(c)
			print(str(a[0]) + ':' + str(a[1]), "connected")
	
    
server = Server()
server.run()
