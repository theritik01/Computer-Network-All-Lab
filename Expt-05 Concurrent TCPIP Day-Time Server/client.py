#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import time
def client_program():
 host = socket.gethostname()
 port = 6215
 client_socket = socket.socket()
 client_socket.connect((host, port))
 while (True) :
     data = client_socket.recv(1024).decode()
     print('Received from server: ' + data)
     break
 client_socket.close()
if __name__ == '__main__':
 client_program()


# In[ ]:




