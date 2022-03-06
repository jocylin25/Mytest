__author__ = 'admin'
#递归函数：自己调用自己

#最大递归深度1000次
# def wahaha():
#     wahaha()
# wahaha()

#递归函数-解决嵌套的列表操作
# lst =['a1','a2',['a11','a22',['b1','b2',['c1','c2']]]]
# def look_up(lst):
#     for i in lst:
#         if type(i) is list:
#             look_up(i)
#         else:
#             print(i)
# look_up(lst)

#练习题：求列表[1,2,3,4[5,6,7,8,[6,3,2,1]]]里所有元素的和
# lst = [1,2,3,4,[5,6,7,8,[6,3,2,1]]]
# sum_n = 0
# def sum_a(lst):
#     global sum_n
#     for i in lst:
#         if type(i) is list:
#             sum_a(i)
#         else:
#             sum_n+=i
#     return sum_n
# ret =sum_a(lst)
# print(ret)

#练习题：递归实现阶乘
# def fn(n):
#     if n >1:
#         return n * fn(n-1)
#     else:
#         return n
# ret = fn(5)
# print(ret)

#

