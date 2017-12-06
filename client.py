import socket                  # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Create a socket object
host =''#socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file.py', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)
	print('here?')
f.close()
print('Successfully get the file')
s.close()
print('connection closed')

from received_file import *
# Program to multiply two matrices using nested loops

# 3x4 matrix
Y = [[5,8],
    [6,7]]
# result is 3x4
result = [[0,0],
         [0,0]]

# iterate through rows of X
for i in range(len(A)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += A[i][k] * Y[k][j]

for r in result:
   print(r)

file=open("/Users/rihardsmurnieks/client/resultata.dat", "w")

for item in result:
        file.write("%s" % item)

file.close()





