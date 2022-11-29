import socket
import sys
import calculator


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
except socket.error as err:
    print("Socket creation failed with error:" %(err)) 

port = 8041
s.bind(('',port))
print('socket binded to %s'%(port))

s.listen(2)

while True:
    c, addr = s.accept()
    print("got connection from ",addr)

    cmd = c.recv(1024).decode()
    
    ret = calculator.calc(cmd)
    if(type(ret) == str):
        c.send(ret.encode())