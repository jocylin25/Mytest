#发送端和包机制：当两条数据很短，且数据发送的间隔非常小，那么就把数据合成一个包发送
#特指tcp协议：流式传输，无边界
import socket
sk=socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()
conn,addr=sk.accept()
conn.send(b'hello')
conn.send(b'world')
conn.close()
sk.close()
