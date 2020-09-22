#更新数据库
#from qqwry import updateQQwry
#ret = updateQQwry('qqwry.dat')

from qqwry import QQwry
q = QQwry()
q.load_file('qqwry.dat')
location=q.lookup('45.79.96.104')
print(location[0])



import socket
 
result = socket.getaddrinfo("45.79.96.104", None)
print(result[0][4][0])