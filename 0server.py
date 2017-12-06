import socket


host=''
port=8888
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print 'Listening to connections'
while True:
	computer1, address = s.accept()
	print 'I am connected to ' + address[0] + ':' + str(address[1])

s.close(1) 
