import socket
import csv 

from threading import *
def main():
	reader=[]
	with open('data.csv') as file:
	    reader = csv.reader(file)
	    print(reader)
	    for row in reader:
	        print(row[1])
    
	s = socket.socket()
	host='10.10.9.54'
	port=5002
	s.bind((host,port))
	s.listen()
	while True:
		c,addr=s.accept()
		message=s.recv(1024).decode()
		attendance=message.split(" ")
		count=0
		for row in reader:
			if attendance[1]==row[0]:
				count=1
				Thread(target = check,args=(row,)).start()

				
		if count=0:
			c.send('ATTENDANCE-FAILURE')
def check(row,):
	while True:
		c.send(row[1].encode())
		answer=c.recv(1024).decode()
		ans=answer.split(" ")
		if ans==row[2]:
			c.send('ATTENDANCE-SUCCESS'.encode())
			break
if __name__=='__main__':
	main()
