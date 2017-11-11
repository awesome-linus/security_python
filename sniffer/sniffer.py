# -*- coding: utf-8 -*-

import socket

# create object
sniff = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# bind data
sniff.bind(('127.0.0.1', 0))

# socket option
sniff.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# sniffer is now active
print('Sniffer is listening!')

# get messages from socket
print(sniff.recvfrom(4096))
