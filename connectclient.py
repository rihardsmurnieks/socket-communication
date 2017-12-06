import socket
import sys
from createjson import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server_address = ('localhost', 8888)

s.connect(server_address)                               

message = 'JSON notation'
print 'sending "%s"' % message
s.sendall(json_string)



try:
	data = s.recv(1024)
	print '%s' % data

finally:
	s.close()
	print 'connection closed'

