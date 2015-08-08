import socket
import time

IP = ""
PORT = 5002
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

iplookup={
    "google.com":"216.58.220.46",
    "quora.com":"54.84.216.68",
    "yahoo.com":"206.190.36.45",
    "facebook.com":"173.252.120.6",
    "reddit.com":"198.41.208.139",
    "gmail.com":"216.58.220.37",
    "medium.com":"50.19.110.10",
    "arjunmayilvaganan.in":"192.30.252.153",
    "stackoverflow.com":"104.16.104.85"
}

while True:
    domain_name, client_address = sock.recvfrom(1024)
    time.sleep(3)
    if iplookup.has_key(domain_name):
        sock.sendto(iplookup[domain_name],client_address)
    else:
        sock.sendto("Sorry. Not available.",client_address)