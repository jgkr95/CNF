from threading import *
import socket
def main():
	s=socket.socket()

	host='10.10.9.54'
	port=5010
	s.connect((host,port))
	print(s.recv(1024).decode())
	s.send(input().encode())
	Thread(target= send,args=(s,)).start()
	while True:
		print(s.recv(1024).decode())
	s.close()
def send(s):
	while True:
		s.send(input().encode())
	s.close()
if __name__=='__main__':
	main()
