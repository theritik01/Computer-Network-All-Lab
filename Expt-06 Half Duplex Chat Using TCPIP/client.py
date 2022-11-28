#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from socket import *
server_name = 'localhost'
server_port = 6969
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))
while True:
 sentence = input(">>")
 client_socket.send(sentence.encode())
 message = client_socket.recv(2048)
 print ("From Server:", message.decode())
 if(sentence == 'q'):
     client_socket.close()


# In[ ]:




