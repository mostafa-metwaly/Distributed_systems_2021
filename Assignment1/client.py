import socket
import sys
import threading

class Client:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def sendMSG(self):
		while True:
			self.sock.send(bytes(input(""),'utf-8'))

	def __init__(self,address):
		self.sock.connect((address,5000))

		iThread = threading.Thread(target=self.sendMSG)
		iThread.daemon = True
		iThread.start()

		while True:

			data = self.sock.recv(1024)
			if not data:
				break
			print(str(data,'utf-8'))



if (len(sys.argv) >1):
	client = Client(sys.argv[1])

else:
	print("please re-enter the ip address")