__author__ = 'admin'
#列表推导式，python特有写法
#例1：l=[1,2,3,4]  得到新列表p[2，4，6，8]
# l=[1,2,3,4]
# p =[2*i for i in l]
# print(p)              #p中所有元素已经存在内存里
#例2：所有偶数存在新列表
l=[1,2,3,4]
s=[i for i in range(1,5) if i%2==0]
print(s)

#生成器表达式
#列表推导式的 [] 换成() 就变成了生成器表达式
# gen =(i*2 for i in range(5))      #gen里什么也没有，通过方法取才有
# print(gen)
#生成器中取值的三种方式
#1. gen.__next__
#2.for n in gen:pass
#3.list(gen)

#迭代器 是一个可以被for 循环的节省内存的类型
#生成器 程序员能够自己写的迭代器
    #生成器函数：yirld
        # g =生成器函数（）
    #生成器表达式
        # g =(表达式)
        #列表推导式和生成器表达式所使用的“表达式相同”
#所有生成器都符合迭代器特点
#1.一个一个取值，而不是一次性把所有数据都创建出来，迭代器中数据不取不创建
#2.只能按照顺序取，不能跳过不能回头
#3.一个迭代器中数据只能从头到尾取一次

#迭代器中取值的三种方式
#1. gen.__next__
#2.for n in gen:pass
#3.list(gen)

#简单的for循环生成新列表 --> 列表推导式联系起来
#只要用到列表推导式  ——>将其转化成生成器表达式
#生成器函数--> 处理文件

#面试题：
#1.生成器+生成器表达式
#写生成器
# def demo():
#     for i in range(4):
#         yield i
# g=demo()
# g1=(i for i in g)
# g2=(i for i in g1)
# #从生成器取值
# print(list(g1))
# print(list(g2)) #没有值，生成器中的值只能从头到尾巴取一次

#2.生成器+for循环 for循环拆开
#定义生成器
# def add(n,i):
#     return n+i
# def test():
#     for i in range(4):
#         yield i
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
# #从生成器取值
# print(list(g))

#3.作业：生成器面试题


#练习1：30以内所有能被3整除的数
# s =[i for i in range(1,30) if i%3==0]
# print(s)
#练习2：30以内所有能被3整除的数的平方
# s =[i*i for i in range(1,30) if i%3==0]
# print(s)
#练习3.找到嵌套列表中名字含有两个e的所有名字
# names =[['Tom','Steven','Joe','Billy',],['Jill','Jennifer']]
# s =[name for lst in names
#         for name in lst if name.count('e')==2]
# print(s)

