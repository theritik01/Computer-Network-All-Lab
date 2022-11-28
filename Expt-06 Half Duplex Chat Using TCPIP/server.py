#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from socket import *
server_port = 6969
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print ("The server is now ready to receive")
connection_socket, address = server_socket.accept()
while True:
 sentence = connection_socket.recv(2048).decode()
 print('From Client:',sentence)
 message = input(">>")
 connection_socket.send(message.encode())
 if(message == 'q'):
     connectionSocket.close()


# In[ ]:




