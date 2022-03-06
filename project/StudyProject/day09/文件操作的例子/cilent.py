import os
import json
import socket
sk =socket.socket()
sk.connect(('127.0.0.1',9001))
#输入需要发送的文件，获取并发送文件大小
file_path=r'E:\python\data\1.txt'
file_name=os.path.basename(file_path)
file_size=os.path.getsize(file_path)
dic={'file_name':file_name,'file_size':file_size}
str_dic=json.dumps(dic)
dic_b=str_dic.encode('utf-8')
sk.send(dic_b)
with open(file_path,mode='rb') as f:
    content =f.read()
    sk.send(content)
sk.close()
