import socket
HN=socket.gethostname()
ipaddress=socket.gethostbyname(HN)
print(ipaddress)
