import socket

IP = "127.0.0.1"
PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

c2s=["init0",""]
prevrply="init1"
s2c=["",""]

while True:
    c2s[1]=raw_input("client: ")
    sock.sendto(c2s[0],(IP,PORT))
    sock.sendto(c2s[1],(IP,PORT))
    s2c[0],servaddr=sock.recvfrom(1024)
    s2c[1],servaddr=sock.recvfrom(1024)
    if s2c[0]==prevrply:
        print 'Server:',s2c[1]
        prevrply=s2c[1]
    else:
        print 'Server:',s2c[0] 
        prevrply=s2c[0]
    c2s[0]=c2s[1]