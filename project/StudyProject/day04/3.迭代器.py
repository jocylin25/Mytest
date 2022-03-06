__author__ = 'admin'
#迭代器
#1.一个一个取值，而不是一次性把所有数据都创建出来
#2.只能按照顺序取值，不能跳过也不能回头
#3.一个迭代器中的数据只能从头到尾巴取一次
#4。不是直接存储了内容，而是需要for循环才能获取每一个值
#可迭代协议：如果一个数据类型中有iter方法，那么这个数据类型就是可迭代类型
#迭代器协议：如果一个数据类型中有iter方法和next方法，那么这个数据类型就是迭代器类型

#可迭代类型不是迭代器
# print('__iter__'in dir('abc'))
# print('__iter__'in dir([1,2,3]))
# print('__iter__'in dir({1,2,3}))
# print('__iter__'in dir((1,2,3)))
# print('__iter__'in dir({1:3}))
# print('__iter__'in dir(range(10)))

#迭代器:文件操作符
# f =open(r'E:\python\data\project\StudyProject\day04\test',encoding='utf-8')
# print('__iter__'in dir(f))
# print('__next__'in dir(f))
#迭代器特点：节省内存空间

#可迭代类型转换成迭代器
# ran = range(0,5,1)    #1:步长
# iterator = ran.__iter__()
# iterator.__next__()
# iterator.__next__()
# iterator.__next__()
# iterator.__next__()

#for循环源码
# l =[1,2,3,4,5]
# iter = l.__iter__()
# while True:
#     try:
#         print(iter.__next__())
#     except StopIteration:
#         break
#所有能被for循环的至少是一个可迭代类型








