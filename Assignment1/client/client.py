import socket
import sys
import threading

class Client:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def sendMSG(self):
		while True:
			self.sock.send(bytes(input(""),'utf-8'))

	def __init__(self):
		self.sock.connect(('0.0.0.0',8989))

		iThread = threading.Thread(target=self.sendMSG)
		iThread.daemon = True
		iThread.start()

		while True:

			data = self.sock.recv(1024)
			if not data:
				break
			print(str(data,'utf-8'))



client = Client()
