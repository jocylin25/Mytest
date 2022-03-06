import socket
#实例化一个socket对象
sk =socket.socket()    #买手机
sk.bind(('127.0.0.1',9000))   #装上电话卡
#开始监听
sk.listen()             #开机
#建立一个连接，一次accept相当于接收一个客户端请求
conn,addr =sk.accept()  #等电话，等待客户连接我  conn就是server与客户端建立起的一个连接
while True:
    msg_send=input('>>>')
    #连接.send (bytes类型)发送消息
    conn.send(msg_send.encode('utf-8'))  #接了电话说hello
    if msg_send.upper()=='Q':
        break
    #连接.recv(n)   接收消息，n代表接收的最大字节
    msg=conn.recv(1024).decode('utf-8')
    if msg_send.upper()=='Q':
        break
    print(msg)
conn.close()    #挂电话
sk.close()      #关手机

