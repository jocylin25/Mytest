__author__ = 'admin'
# a=2
# b=3
# #三元运算符
# max_num =a if a>b else b     #a>b  成立  max_num=a  否则max_num=b

#匿名函数  ：
# 又称lambda表达式，如果一个函数中功能很小，只有一句代码，则可以把这个函数创建成一个匿名函数
#形式： lambda 参数：返回值          没有return
# func2 =lambda a,b:a+b
# ret = func2(3,4)
# print(ret)
# print(func2.__name__)

#func2.__name__  获取后为固定值<lambda>

#练习题：
# lambda表达式a,b两个值，求较大的值
# func1 =lambda a,b:a if a>b else b
# max_num = func1(3,4)
# print(max_num)
# lambda表达式a为参数，求a的奇偶性
# func2 =lambda a:'偶数' if a%2==0 else'奇数'
# num = func2(5)
# print(num)
# lambda表达式a为参数，求a绝对值
# func3 = lambda a:a if a>0 else -a
# value =func3(-8)
# print(value)

#lambda 可以不传参 参数用空格代替
# func =lambda : 2+3
# ret = func()
# print(ret)