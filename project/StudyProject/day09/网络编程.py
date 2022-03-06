#B/S 架构 ：轻量级，是特殊的c/s 架构
#C/S 架构：安全性 历史数据的保存
#PC端：B/S统一了入口
#移动端：小程序、支付宝

#socket代码实现聊天实例：套接字

#网络通信协议：
# TCP
    #保证数据传输的可靠性
    #占用连接：
        # 建立连接：三次握手 ：第一次发SYN第二次回SYN、ACK第三次发ACK全双工通信
        #开始通信 ：发邮件/文件上传、下载
        #断开连接：四次挥手 发FIN 回ACK，发FIN 回ACK
    #指定参数
        # socker(family=socket代码实现聊天实例.AF_INET, type=socket代码实现聊天实例.SOCK_STREAM)
        #socker() 不写默认tcp
# UDP
    #不占连接，不可靠性
    #不需要建立连接，直接互传即可
    #指定参数
        # socker(family=socket代码实现聊天实例.AF_INET, type=socket代码实现聊天实例.SOCK_DGRAM)
        #family=socket代码实现聊天实例.AF_INET 基于网络通信  type=***  基于***通信
