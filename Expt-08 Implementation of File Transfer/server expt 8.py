#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket 
port = 6443
s = socket.socket() 
host = socket.gethostname() 
s.bind((host, port)) 
s.listen(5) 
print ('Server listening....')
while True:
    conn, addr = s.accept()
    print ('Got connection from', addr)
    fileToBeOpened = conn.recv(1024).decode()
 
    filename='C:/Users/ritik/OneDrive/Desktop/'+fileToBeOpened
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print('Sent: ',l.decode('utf-8'))
        l = f.read(1024)
    f.close()
    print('Done sending')
conn.close()


# In[ ]:




