#__author__ = 'admin'
#回顾：
#文件操作
    #打开文件
        #open('文件路径'，mode='r',encoding='utf-8')  #转译成指定编码格式
        #open('文件路径'，mode='w',encoding='utf-8')
        #open('文件路径'，mode='a',encoding='utf-8')
        #open('文件路径'，mode='rb')        #直接读，打开文件不需要指定编码，需手动转译
        #open('文件路径'，mode='wb')
        #open('文件路径'，mode='ab')
    #读写文件
    #读
        # read()  #读全部
        # read(n)  #读n个字节/字符
        # readline() #每次读一行 ，记录光标，不知道什么时候结束
        # for a in b:
        #写
        # write('想写啥写啥')
        # write(b'abc')   #字节型  以rb形式打开时
    #关闭文件
        #f.close()
    #删除和修改文件
        #删除文件
        # import os
        # os.remove('文件绝对路径')
    #文件改名
        #os.rename('原名','目的名')
    #修改文件
        #读a文件 写b文件
        #删除a，重命名b

#初识函数
    #定义
    # def 函数名（形参）：
    #     函数体
    #     return 返回值
    #调用
        # 变量名 = 函数名（实参）
        # 变量就是函数的返回值
    #返回值
        # 1.不写默认返回none
        # 2.只写return 表示函数结束 返回none
        # 3.return 值
    #参数
        # 按照位置传参
        # 按照关键字传参
        # 先位置，再关键字
        #调用者角度
            # cal(1,2,3)
            # cal(a=1,b=2,c=3)
            # cal(1,b=2,c=3)
            # cal(1,2,c=3)
            # l =[1,2,3]
            # cal(*l)  #-->cal(l[0],l[1],l[2])
        #定义函数角度
            # 位置参数
            # *args 动态参数
            # 默认参数
            # **kwargs 动态参数
            # def cal(a,b,*args,c=3,**kwargs):
            #     pass
#练习题：参数的陷阱，如果参数默认的值是一个可变数据类型，那么所有的调用者都共享这一个数据
#l =[]这个变量在定义的时候创建一次，不会在调用的过程中再次被创建了
# def func(a,l =[]):
#     l.append(a)
#     print(l)
# func(1)
# func(2,[])
# func(3)