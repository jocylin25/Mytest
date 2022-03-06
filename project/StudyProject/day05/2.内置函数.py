__author__ = 'admin'
#局部变量
#locals()
#全局变量
#globals()
#输入打开
# input()
# open()
#id() 查看变量内存地址
#eval() exec()
# 要注意使用的安全性
#从文件读出、用户输入的、从网络中获取的 不要直接用eval()
#eval() :把字符串组成的内容当python代码执行，并返回值
# ret = input('<<<')
# print(eval(ret))
# def func():
#     print('执行了func')
# eval('func')()
#exec():把字符串组成的内容当python代码执行,无返回值
# def func1():
#     print('执行了func1')
# exec('func1()')

#callable 检测某一个名字是否可以被调用 ，名字后面可以加（）
# a =1
# print(callable(a))
# a =lambda :1
# print(callable(a))
#dir 帮助函数
# 1.查看一个数据可以调用哪些方法
#2.也可以通过看某一个特定方法是不是在这个结果中，以此来判断这个数据的类型
# ret = dir(range(10))
# print(ret)

#print()
#向屏幕所在的文件输出内容
# end 结束符
# sep 分隔符
# print(1,2,3,end = '$')
# print(1,2,3,sep = ':')
#向指定文件输出内容
# with open('print_test','w') as f:
#     print('wahaha',file=f)

#数学类
#abs(m)        计算m绝对值
#divmod(m,n) 求商余  m除数 ，n被除数  返回（商，余）
#round(小数，精确位数)     小数精确
#pow (m,n) 幂运算  m的n次幂  同m**n
#sum(Iterator)
#min（Iterator)
#min（Iterator，key=)   key=abs  ,key=匿名函数
#max(Iterator)

#ord ('a')   ASCII转编码
# chr ('97')  编码转ASCII
# repr()    打印某个变量值时便于区分数据类型
#l.reverse()  列表的反转函数  ，列表本身改变
#reversed(l) 列表的反转函数  ，列表本身不变,返回的是迭代器不是列表

#filter(func,lst)  生成器函数 返回值是一个迭代器
# lst =[1,2,3,4,5]
# ret = filter(lambda n:n%3==0,lst)
# for i in ret:
#     print(i)

#map(func,lst)  返回值是一个迭代器
#enumerate(iterable,1)    枚举函数 给iterable添加序号
#zip 拉链方法  对应位置都有数据的拉在一起
# a =[1,2]
# b =['a','b']
# c=['换手率','涨跌幅']
# ret=zip(a,b,c)
# for i in ret:
#     print(i)

# sorted（lst）排序  默认升序排  reverse=True降序排  key=abs 按照绝对值


#练习题[{'age':18}，{'age':8}，{'age':28}] 按照升序排列

#练习题：九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%2s'%(j,i,i*j),end='')
#     print(i,j)
#练习题：模拟进度条
#面试题：(('a','b'))  (('c','d '))两个元组，使用匿名函数生成列表[{'a':'c'},{'b':'d'}]
# tup1 =(('a','b'))
# tup2 =(('c','d '))
# ret =zip(tup1,tup2)
# ret1 =list(ret)
# lambda i:for
# for i in ret:
#     print(i)