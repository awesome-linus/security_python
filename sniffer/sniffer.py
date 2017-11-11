import socket

sniff = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

sniff.bind(('127.0.0.1', 0))

sniff.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL, 1)

print('Sniffer is listening!')

print(sniff.recvfrom(4096))