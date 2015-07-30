import socket

IP = ""
PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

s2c=["initial1",""]
prevrply="initial0"
c2s=["",""]

while True:
    c2s[0],cliaddr = sock.recvfrom(1024)
    c2s[1],cliaddr = sock.recvfrom(1024)
    if c2s[0]==prevrply:
        print 'Client: ',c2s[1]
        prevrply=c2s[1]
    else:
        print 'Client: ',c2s[0] 
        prevrply=c2s[0]
    s2c[1]=raw_input("Server: ")
    sock.sendto(s2c[0],(IP,PORT))
    sock.sendto(s2c[1],(IP,PORT))
    s2c[0]=s2c[1]