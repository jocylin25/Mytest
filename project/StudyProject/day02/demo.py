__author__ = 'admin'
# coding=gbk
#格式化输出
# name = input('姓名：')
# print('welcome %s'%name)
# print('welcome %s'%20)
# print('welcome %d'%20)

#列表
# lst = ['张','钱','孙','李']
# print(lst)
#索引
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[-1])     #最后一个元素
# print(lst[-2])     #倒数第二个元素
# print(lst[-3])
# print(lst[-4])

#切片
# print(lst[:])          #全部元素
# print(lst[:2])         #第0个元素切到第2个元素之前
# print(lst[2:])         #从第2个元素开取
# print(lst[1:2])        #取左不取右
# print(lst[-3:-1])       #倒数第3个取到倒数第2个元素  省略1：step
# print(lst[-3:-1:1])     #倒数第3个取到倒数第2个元素  1：step
# print(lst[-1:-3:-1])    #从倒数第1个取到倒数第2个元素   -1：step
# print(lst[-1:-3])       #错误，-1：step不可省略
# print(lst[::2])         #从第0个元素隔两个取
# print(lst[::-1])        #列表翻转

#列表的拷贝
# lst2 = lst[:]
# lst3 = lst[::]
# lst4 = lst.copy()

#增加元素
#lst.append('贾淑媛')
#删除元素
#
#练习1：描述一个人的姓名密码年龄
# name = input('name:')
# password = input('password:')
# year = input('year:')
# lst5 =[]
# lst5.append(name)
# lst5.append(password)
# lst5.append(year)
# print(lst5)

#值的引用
#列表浅拷贝  内存地址共用
# l =[1,2,['linda','25'],'3']
# print(len(l))
# for n in l:
#     print(n)
# l1 = l[:]
# l2 = l.copy()
# l2[2].append('hellokitty')
# print(l)
# print(l1)
# print(l2)

#深拷贝  内存地址全部拷贝一遍 拷贝浪费内存不建议
# import copy
# l2 = copy.deepcopy(l)
# l2[2].append('hellokitty')
# print(l)
# print(l2)

#查看索引位置
# l.index('查找内容')

#enumerate 方法，将列表中的元素元组化,输出列表元素和序号
lst  = ['alex','eric','rain','linda','david','wind']
print(list(enumerate(lst)))

#通用操作
    # in  not in 判断一个元素在不在列表里

#练习2：
# 循环3次
# 输入用户名，若存在提示：已经存在 未存在，把这个名字添加进列表，
# 打印列表
# n = 0
# lst =[]
# while n <3:
#     name = input('请输入姓名：')
#     if name in lst:
#         print('用户%s已存在'%name)
#     else:
#         lst.append(name)
#     n=n+1
# print(lst)

#练习3 用户输入用户名和密码，只要用户名和密码对上了l中的值，显示登陆成功，否则显示登录失败
# l=[['alex','222'],['wusir','666'],['周老板','123456']]
# name = input('输入姓名：')
# passwd = input('输入密码：')
# for item in l:
#     if name==item[0] and passwd==item[1]:
#         print('登陆成功')
#         break
# else:
#     print('登陆失败')

#判断字符串是不是完全用数字组成
#s =' a '
#s1 =s.upper()
#s1=s.replace('a','v')
# s2 =s.strip()
# s2 =':'.join(['alex','3214','86'])
# print(s2)
#s1 = s.split(';')
#s2 = s.strip('<>')
#print(s2)
#print(s.isdigit())
#print(s.isalpha())

#元组
#days =('星期一','星期二','星期三','星期四','星期五')
#字典
d= {
        'alex':'123',
        'david':'456'
    }
d['alex']=='123'