import socket
import time

IP = "127.0.0.1"
PORT = 5002
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setblocking(0)
meaning_word = "null"

while True:
    msg = raw_input("enter the word :")
    while(meaning_word == "null"):
        sock.sendto(msg,(IP,PORT))
        time.sleep(3)
        try:
            meaning = sock.recvfrom(1024)
            meaning_word=meaning[0]
            meaning_addr=meaning[1]
            print "server reply :" + meaning_word
        except: 
                print "retransmit"
