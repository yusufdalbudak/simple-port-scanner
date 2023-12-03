import socket

ip='192.168.56.101'

for port in range(1,100):
 try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    print(str(port),": open")
 except Exception as e:
    print(str(port),": closed")
    pass
 finally:
    s.close()

