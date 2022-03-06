#接收文件
import json
import socket
sk =socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()
conn,addr =sk.accept()
file_dic =conn.recv(1024).decode('utf-8')
dic = json.loads(file_dic)

with open(dic['file_name'],mode='wb') as f:
    while dic['file_size']>0:
        file_content=conn.recv(1024)
        dic['file_size'] -=len(file_content)
        f.write(file_content)
conn.close()
sk.close()
