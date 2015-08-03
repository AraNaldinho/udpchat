import socket
import time

IP = ""
PORT = 5002
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

ram_meaning = "cute"
sam_meaning = "mass"

while True:
    word , cliaddr = sock.recvfrom(1024)
    time.sleep(5)
    if(word == "ram"):
        sock.sendto(ram_meaning,cliaddr)
    elif(word == "sam"):
        sock.sendto(sam_meaning,cliaddr)
