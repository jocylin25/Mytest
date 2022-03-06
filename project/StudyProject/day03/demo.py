# coding=gbk
# 1.求100以内的素数和（除了1和本身不能被其他数整除）
# sum = 0
# for i in range(2,101):
#     for j in range(2,i//2+1):
#         if i%j ==0:
#             break
#     else:
#         print(i)
#         sum +=i
# else:
#     print('素数和为%s'%sum)

#文件操作
#读
# f =open(r'E:\python\data\project\StudyProject\day03\userinfo',
#         mode ='r',
#         encoding='utf-8')
# print(f.read())
# f.close()
#写
# f =open(r'E:\python\data\project\StudyProject\day03\userinfo',
#         mode ='w',
#         encoding='gbk')
# f.write('\n小贾：27')
# f.close()
# f =open(r'E:\python\data\project\StudyProject\day03\userinfo',
#         mode ='a',
#         encoding='gbk')
# f.write('\n小贾：26')
# f.close()

#函数
# lst =[1,2,3,4]
# #函数的定义
# def mylen():
#         i = 0
#         for j in lst:
#                 i+= 1
#         print(i)
# #函数的调用
# mylen()

#练习题1 写函数，a b c 三个值，计算a*b/c的结果并打印
# a =1
# b =2
# c =3
# def abc():
#         s = a*b/c
#         return s           #返回值
# ret = abc()
# print(ret)
#
# def sum(a,b,c):  #形式参数
#     return a+b+c
# ret =sum(1,2,3)     #实参
# print(ret)
#练习题2 写函数，传入两个参数，比较两个参数的大小，并返回较大的那一个数值
# def ab(a,b):
#     if a>b:
#         return a
#     else:return b
# a = input('输入a的值')
# b = input('输入b的值')
# v =ab(int(a),int(b))
# print(v)

#练习3 列表/元组/字符串/字典 求两个类型的长度比，返回数据长度更长的类型
# def mylen(seq):
#     i =0
#     for j in seq:
#         i +=1
#     return i
# def compare(seq1,seq2):
#     if mylen(seq1)>mylen(seq2):
#         return seq1
#     else:
#         return seq2

#局部修改全局变量
# a =1
# def func():
#     global a
#     a +=1
#     print(a)
# func()

#高阶函数
# f=1
# def outer():
#     f=2
#     def inner():
#         nonlocal f
#         f =f+1
#         print('inner',f)
#     inner()
#     print('outer',f)
# print('全局',1)
# outer()