#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import time
def server_program():
 host = socket.gethostname()
 port = 6215
 server_socket = socket.socket()
 server_socket.bind((host, port))
 server_socket.listen(5)
 conn, address = server_socket.accept()
 print ( "Connection from: " + str (address))
 while True:
     ti = time.gmtime()
     data = (time.asctime(ti))
     conn.send(data.encode())
     print('Day/Time: ' + data)
     break
 conn.close()
if __name__ == '__main__':
 server_program()


# In[ ]:




