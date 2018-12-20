import socket

def Main():
	host = '10.10.9.54'
	port = 1245
	s = socket.socket()
	s.connect((host,port))
	
	data = s.recv(1024)
	print("Recieved from: " + str(data.decode()))
	message = input("-->")
	while True:
		s.send(message.encode())
		data = s.recv(1024)
		print("Recieved from Server: " + str(data.decode()))
		dat = data.decode().split()
		if (dat[0] == 'Correct,' or message == 'q'):
			s.send('q'.encode())
			break
		message = input("-->")
	s.close()
if __name__ == '__main__':
	Main()