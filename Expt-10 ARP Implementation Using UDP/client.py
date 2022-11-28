#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',6968))
add = input('Enter IP: ')
s.send(add.encode())
mac = s.recv(1024)
mac = mac.decode('utf-8')
print('MAC of',add,' is: ',mac)


# In[ ]:




