from threading import *
import socket
def main():
	
	s=socket.socket()

	host='10.10.9.54'
	port=5002
	s.connect((host,port))
	s.send('MARK-ATTENDANCE '+input(Enter Roll number).encode())

	while True:
		message=s.recv(1024).decode()
		if message='ROLLNUMBER-NOTFOUND':
			print('ROLLNUMBER-NOTFOUND')
			break
		elif message='ATTENDANCE-FAILURE':
			print(s.recv(1024).decode())
			s.send('SECRETANSWER '+input().encode())
		elif meassage='ATTENDANCE-SUCCESS':
			s.close()
		else:
			print(s.recv(1024).decode())
			s.send('SECRETANSWER '+input().encode())
	s.close()
if __name__=='__main__':
	main()
