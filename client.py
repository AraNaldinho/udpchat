import socket
import time

IP = "127.0.0.1"
PORT = 5002
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setblocking(False)

while True:
    domain_name = raw_input("Enter the domain name: ")
    site_ip = None
    while(site_ip == None):
        sock.sendto(domain_name,(IP,PORT))
        time.sleep(2)
        try:
            site_ip, server_address = sock.recvfrom(1024)
            print "Corresponding IP:",site_ip
        except: 
                print "Retransmitting"