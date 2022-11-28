#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
localIP = "127.0.0.1"
localPort = 6191
bufferSize = 1024
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
 bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
 message = bytesAddressPair[0]
 address = bytesAddressPair[1]
 clientMsg = "Message from Client:{}".format(message)
 clientIP = "Client IP Address:{}".format(address)
 print(clientMsg)
 print(clientIP)
 # Sending a reply to client
 bytesToSend = message
 UDPServerSocket.sendto(bytesToSend, address)


# In[ ]:




