import socket
from threading import *
def main():
	s = socket.socket()
	host='10.10.9.54'
	port=5010
	s.bind((host,port))
	s.listen(10)
	lis={}
	li = []
	while True:
		c,addr=s.accept()
		c.send('Enter username'.encode())

		usern=c.recv(1024).decode()
		print(usern+' Connected........')
		lis[c]=usern
		li.append(c)

		Thread(target = chat,args=(lis,c,li)).start()
	s.close()
def chat(lis,c,li):
	while True:
		# print('Inside While')
		# print('Inside try')
		message=c.recv(1024).decode()
		if(message!='q'):
			print('Inside QQQ')
			for user,val in lis.items():
				# print(user + ' -- ')
				print('Dict')
				
				if c != user:
					user.send((lis[c]+'-->'+message).encode())
				else:
					c.send(('Me==>'+message).encode())
		else:
			c.close()
			lis.pop(c)
			li.remove(c)
			return 1
if __name__=='__main__':
	main()


