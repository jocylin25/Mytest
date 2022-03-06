#协程：由程序控制，对于IO操作敏感度较低，只有和网络相关操作用到
#优点：可以开的个数更多
#安装gevent模块
#
from gevent import monkey
monkey.patch_all()       #给下面阻塞打包

from gevent import socket
import gevent      #gevent在识别阻塞之后，会在遇到阻塞之后自动识别

def func(conn):
    while True:
        conn.send(b'hello')  #msg必须是字节类型
        message =conn.recv(1024) #接收消息的最大字节数
        print(message)
if __name__ == '__main__':
    sk=socket.socket()
    sk.bind(('127.0.0.1',9001))
    sk.listen()
    while True:
        conn,addr =sk.accept()   #接收客户端请求建立连接 --三次握手
        gevent.spawn(func,conn)         #开启协程
    conn.close()