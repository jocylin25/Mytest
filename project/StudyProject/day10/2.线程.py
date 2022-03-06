#线程开启速度比进程快
#由操作系统控制，对于IO感知能力非常强
#进程线程区别：
    # 进程内存隔离，占用资源多
    # 线程内存共享的，占用资源少
#python线程：cptyhon解释器下的多线程，
    # 同一个进程下的多个线程不能被CPU同时执行
    #多个线程中的IO操作仍会被规避
    #大部分涉及文件、网络操作，多线程更快
    #真正参与计算的都是那几个cpu
        #规避IO操作，让IO操作时间尽量缩短
        #或尽量复用这部分时间
import time
from urllib import request
from threading import Thread
url_lst=[
    'http://www.baidu.com',
    'http://www.sogou.com',
    'http://www.qq.com',
    'http://www.163.com',
    'http://www.jd.com',
    'http://www.tmall.com',
    'http://www.mi.com',
]
#方式一：
def get_url(url):
    ret =request.urlopen(url)    #请求一个网页
start_t =time.time()
t_lst=[]
for url in url_lst:               #开启10个线程，同时请求10个网页
    t=Thread(target=get_url,args=(url,)) #args 元组
    t.start()
    t_lst.append(t)
for t in t_lst:
    t.join()     #等待十个请求结束
print(time.time()-start_t)

#方式二：
# start_t =time.time()
# for url in url_lst:
#     ret =request.urlopen(url)
# print(time.time()-start_t)