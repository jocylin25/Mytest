#时间模块
# 和时间相关的模块，已封装好
#import time
#获取当前时间,格林威治时间
#time.time()
#让程序暂停执行n秒
#time.sleep(n)
#获取当前时间
#time.strftime('%Y-%m-%d %H:%M:%S')

#函数名
#1.并不是只有函数名（）才能调用函数,只要是函数的地址对应的变量都可以通过（）调用函数
#2.函数的名字可以被赋值，可以作为一个容器类型的元素
#3.变量怎么使用，函数的名字就可以怎么用
# def a():
#     print('in a')
# a()
# print(a)
# b=a
# print(b)
# b()
# l =[a]
# print(l[0])
# l[0]()
#4.函数的名字可以作为另一个函数的参数
# def wahaha(f):
#     f()
# wahaha(a)
#5.函数名可以作为返回值
# def sb():
#     def b():
#         print('in b')
#     return b
# funcb=sb()
# funcb()

#闭包：小局部作用域使用大的局部作用域的变量
# def wahahaha():
#     name ='alex'
#     def a():
#         #内置函数引用了外层函数的变量，a（）就是闭包函数
#         print(name)
#     return a

#不是闭包函数
# def wahahaha():
#     name ='alex'
#     def a(name):
#         print(name)

#是闭包
# def wahahaha(name):
#     def a():
#         print(name)

#不是闭包，不能引用全局变量
# name ='alex'
# def wahahaha():
#     def a():
#         print(name)

#作用：
#from  urllib import request   #url模块
#请求网页，获取网页源码
# ret = request.urlopen('https://www.cnblogs.com/Eva-J/p/7277026.html')
# print(ret.read().decode('utf-8'))

# def get_source_html(url):
#     ret = request.urlopen(url)
#     return ret.read().decode('utf-8')
# blog = get_source_html('https://www.cnblogs.com/Eva-J/p/7277026.html')
# print(blog)

#高阶函数闭包方式请求网页
# def get_source_html(url):
#     dic = {}
#     def get_url():
#         if url in dic:
#             return dic[url]
#         else:
#             ret = request.urlopen(url)
#             dic[url]=ret
#             return ret.read().decode('utf-8')
#     return get_url()
# blog = get_source_html('https://www.cnblogs.com/Eva-J/p/7277026.html')
# print(blog)
# print(blog)
# print(blog)
# print(blog)

#装饰器
#例：计算执行时间
# def timer(funcname):     #funname是func的内存地址
#     def inner(*args,**kwargs):
#         start = time.time()          #执行func之前记录时间
#         ret =funcname(*args,**kwargs)
#         return ret
#     return inner
# @timer                          #相当func =timer(func)    #func=inner内存地址
# def func(n,m):
#     sum_num=0
#     for i in range(n):
#         sum_num +=i             #执行func后计算执行效率
#     return sum_num
#
# @timer                           #相当于func2 =timer(func2)    #func2=inner内存地址
# def func2():
#     sum_num =0
#     for i in range(100000000):
#         sum_num +=i         #执行func后计算执行效率
#     return sum_num
#
# ret1 =func(10000,20)           #调用func，实际调用inner
# ret2 =func2()       #调用func2，实际调用inner
# print(ret1,ret2)

#装饰器什么情况用
    #开放封闭原则
        #开放,对扩展开放
        #封闭，对修改封闭
    #写好一些装饰器加在需要装饰的函数上面

#装饰器固定格式：
# def 装饰器的名字(func):
#     def inner(*args,**kwargs):
#         '''在执行被装饰的函数之前要做的事'''
#         ret =func(*args,**kwargs)          #被装饰函数的返回值
#         '''在执行被装饰的函数之前要做的事'''
#         return ret
#     return inner

#练习题：登陆，把打印在屏幕上的内容写到operate.log文件里做成一个日志文件
# import time
# from functools import wraps   #wrap 已封装好的装饰器  加上后被装饰的函数输出后输出实际的值
# def wrapper(func):     #funname是func的内存地址
#     @wraps(func)                    #wrap 已封装好的装饰器  加上后被装饰的函数输出后输出实际的值，不加输出inner（）值
#     def inner(*args,**kwargs):
#         ret =func(*args,**kwargs)
#         t =time.strftime('%Y-%m-%d %H:%M:%S')
#         with open('operate.log',mode='a',encoding='utf-8') as f:
#             f.write('%s[%s]执行了%s函数'%(t,args[0],func,__name__))               #__name__：以字符串格式获取函数名字 同redister.__name__
#         return ret
#     return inner
#
# @wrapper
# def login(name):
#     print('登陆啦'%name)
# @wrapper
# def register(name):
#     print('注册啦'%name)
# login('alex')
# register('alex')
# #获取函数名
# print(register.__name__)

# def func(a,b):
#     '''
#     函数的注释：作用
#     ：param a:int 长方形的宽
#     ：param b:int 长方形的长
#     ：:return:int 长方形的面积
#     '''
#     return a+b
# #获取函数的注释
# print(func.__doc__)

#一个函数被多个装饰器装饰，执行顺序inner1之前、inner2之前、wahaha、inner2之后、inner1之后
# def wrapper1(func):
#     def inner1(*args,**kwargs):
#         print('inner1之前')
#         ret =func(*args,**kwargs)          #被装饰函数的返回值
#         print('inner1之后')
#         return ret
#     return inner1
#
# def wrapper2(func):
#     def inner2(*args,**kwargs):
#         print('inner2之前')
#         ret =func(*args,**kwargs)          #被装饰函数的返回值
#         print('inner2之后')
#         return ret
#     return inner2
#
# @wrapper1
# @wrapper2
# def wahaha():
#     print('wahaha')
# wahaha()

