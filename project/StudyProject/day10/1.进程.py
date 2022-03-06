#IO操作
#输入input:
    #recv  recvfrom input  read  load
#输出output:
    #send sendto print erite  dump
#输入输出不占用CPU
#纯计算：不涉及任何输入输出，单纯对内存中数据进行操作
#进程：进行中的程序。所有的程序/文件，执行起来之后叫进程
#进程是计算机中资源分配的最小单位
#进程可以被操作系统调度\cpu执行
#一个进程创建时 必须创建大量的内存资源 文件资源 程序代码
#一个进程结束时必须被销毁 总是被父进程销毁掉
#进程与进程间有父子关系
#python代码中的进程都是子进程，写的程序本身是子进程的父进程

#并发进程
import os
import time
from multiprocessing import Process
def func(参数1,参数2):
    print('一个子进程',os.getpid(),参数1,参数2)
    time.sleep(2)

if __name__ == '__main__':   #当本文件被导入的时候不执行if条件中代码
    p =Process(target=func,args=(1,2))
    p.start()         #开启进程
    p.join()          #join()阻塞，等待子进程执行完毕
    print('子进程执行完了')

#每一个进程在运行的过程中会被分配一块属于自己的内存，进程之间内存隔离
#cpu在多个进程之间进行轮转执行进程的任务
#并行：如果两个进程在两块cpu同时执行
#并发：两个进程在一个cpu上轮流被执行

#查看进程在操作系统中的唯一标识
# import os
# os.getpid()
#同时启动多个进程
# from multiprocessing import Process
# def func1():
#     print(123,os.getpid())
# def func2():
#     print('aaa',os.getpid())
# if __name__ == '__main__':
#     Process(target=func1).start()
#     Process(target=func2).start()

