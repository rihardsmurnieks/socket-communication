import socket
import json

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket server created'
server_address = ('localhost', 8888)
sock.bind(server_address)
print 'Sock bind complete'
sock.listen(5)
print 'Server now listening'

while True:
	connection, client_address = sock.accept()
	print 'Got connection from %s' % client_address[0], str(client_address[1])

	
	try:
		while True:
			data=connection.recv(1024)
			print 'received "%s"' % data
			parsed_json=json.loads(data)
			#print 'name is %s' % parsed_json['author']
			if data:
				with open('received_file.txt','a') as f:
					print 'file opened'
					f.write(parsed_json['author'])
					f.write(' has posted new information')
					f.write("\n\n")
					f.write('The title of it is: ')
					f.write(parsed_json['title'])
					f.write("\n\n")
					f.write('Information: ')
					f.write("\n\n")
					f.write(parsed_json['body'])
					f.write("\n\n\n")
				f.close()
				connection.sendall('successfully posted info')
				#print 'sending data back to the client'
				#connection.sendall(data)
			else:
				break
	except ValueError:
		print ''
				
	connection.close()


sock.close()

