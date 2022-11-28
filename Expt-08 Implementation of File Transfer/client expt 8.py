#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket 
s = socket.socket() 
host = socket.gethostname()
port = 6443
s.connect((host, port))
filename = input('Enter Filename: ')
s.send(filename.encode())
print('Receiving data...')
while True:
    data = s.recv(1024).decode()
    print(data)
    fileReceived = data
 
    filenameReceived='C:/Users/ritik/OneDrive/Desktop/'+filename
    with open(filenameReceived,'w+',encoding = 'utf-8') as f:
        f.write(fileReceived)
    f.close()
    if not data:
        break
    print('Successfully got the file')
s.close()
print('Connection closed')


# In[ ]:




