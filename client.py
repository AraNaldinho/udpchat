import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
c2smsg=["initial",""]
prevrply="initial"
currrply="initial"
host = '10.42.0.1';
port = 8888;
while(1):
    c2smsg[0]=c2smsg[1]
    c2smsg[1] = raw_input('Enter message to send : ')
    if c2smsg[1]=="exit":
        s.sendto("client exitted", (host, port))
        break
     
    try :
        #Set the whole string
        s.sendto(c2smsg[0], (host, port))
        s.sendto(c2smsg[1], (host, port))
         
        # receive data from client (data, addr)
        s2cmsg0 = s.recvfrom(1024)
        s2cmsg1 = s.recvfrom(1024)
        prevrply = s2cmsg0[0]
        if prevrply == currrply or prevrply=="initial":
            currrply = s2cmsg1[0]
        else:
            currrply = s2cmsg0[0]
         
        print 'Server reply : ' + currrply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

