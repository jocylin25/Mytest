#两边任意一边输入q，挂电话
import socket
#实例化一个socket对象
sk =socket.socket()    #买手机
#请求连接
sk.connect(('127.0.0.1',9000))
while True:
    #sk对象.recv(n)   sk对象.send(***)
    msg =sk.recv(1024).decode('utf-8')       #字节  直到有数据发过来
    if msg.upper()=='Q':
        break
    print(msg)
    msg_send=input('>>>')
    #连接.send (bytes类型)发送消息
    sk.send(msg_send.encode('utf-8'))  #发送的字节  字符串转字节encode
    if msg_send.upper()=='Q':
        break
sk.close()