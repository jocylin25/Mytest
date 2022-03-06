#模块
#1.什么是模块？
    #py文件
    #自定义模块 把多行代码拆成多个文件使代码更加严谨
#2.导入模块
    #from 模块 import  包
    #import  模块
        #访问变量的值：模块.变量
#3.导入包
    #from 包.包.包   import  模块
        #访问变量的值：模块.变量
    #import 包.包.模块
        # 访问变量的值：包.包.模块.变量名

#模块的导入
#import 模块名
#from 模块名 import 变量名
#from 模块名 import 变量名1，变量名2
#from 模块名 import 变量名1 as 新名1，变量名2 as 新名2
#from 模块名 import *          #导入所有模块

#第一种方式:
# import demo
# print(demo.a)
# print(demo.b)
# demo.func()
#第二种方式:
# from demo import a
# from demo import b
# from demo import a,b,func
# print(a)
# print(b)
# func()

#重命名
# from demo import a as abc,b as bcd
# print(abc,bcd)

