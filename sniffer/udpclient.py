# -*- coding: utf-8 -*-

import socket

target_host = "127.0.0.1"
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto(b"12345", (target_host, target_port))

# receive data
data, addr = client.recvfrom(4096)

# display on terminal
print(data)
