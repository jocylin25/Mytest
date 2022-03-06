# coding=gbk
#__author__ = 'admin'
'''
day01-作业
1.简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型
    编译型 ：每次修改都先编译再执行。java
    解释性：每次修改后不需要重新编译，写好的代码交给解释器，执行速度慢，python
2.执行 Python 脚本的两种方式是什么
    第一种在python解释器中直接输入代码
    第二种代码写入.py文件内，cmd 窗口执行 python +文件路径
3.Pyhton 单行注释和多行注释分别用什么?
    单行注释#  多行注释 三引号
4.布尔值分别有什么?
    true 真 false 假
5.声明变量注意事项有那些?
    变量名只能是数字字母下划线组成
    不能以数字开头
    不能是关键字
6.如何查看变量在内存中的地址?
    用id()函数
var1 = 1
print(id(var1))
7.现有如下两个变量,请简述 n1 和 n2 是什么关系?  ???
n1 = 1
n2 = n1
n1的值1赋给了n2，如果n1的值改变，n2的值不会改变，依然是1
'''
#代码实现：
# 1.实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!(已完成)

# account = input('用户名:')
# password = input('密码：')
# account1 = 'seven'
# password1 = '123'
# if account==account1 and password ==password1  :       #比较字符串 ==
#     print('登陆成功')
# else:
#     print('登陆失败')

# 2.实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次(已完成)
# n =0
# while n<3:
#     account = input('用户名:')
#     password = input('密码：')
#     account1 = 'seven'
#     password1 = '123'
#     if account==account1 and password ==password1  :       #比较字符串 ==
#          print('登陆成功')
#          break
#     else:
#         print('登陆失败')
#         n = n+1

# 3.实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次(已完成)
# n =0
# while n<3:
#     account = input('用户名:')
#     password = input('密码：')
#     account1 = 'seven'
#     account2 = 'alex'
#     password1 = '123'
#     if account==account1 or account == account2 and password ==password1  :       #比较字符串 ==
#          print('登陆成功')
#          break
#     else:
#         print('登陆失败')
#         n = n+1

# 4. 使用while循环实现输出2-3+4-5+6...+100 的和

# 5. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12

# 6. 使用 while 循环实现输出 1-100 内的所有奇数 已完成
# n = 1
# while n<100:
#     if n%2==1:
#         print(n)
#     n=n+1
# 7. 使用 while 循环实现输出 1-100 内的所有偶数  已完成
# n = 1
# while n<100:
#     if n%2==0:
#         print(n)
#     n=n+1
# 8.使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束

# 9.使用while,完成以下图形的输出
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# 10：猜年龄游戏 (已完成)
# 要求：
# 允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
# n = 0
# while n<3:
#     age = input('请输入年龄：')
#     age = int(age)
#     if age==30:
#         print('恭喜！')
#         break
#     n = n+1

# 11：猜年龄游戏升级版
# 允许用户最多尝试3次
# 每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
# 如何猜对了，就直接退出
n = 0
while n<3:
    age = input('请输入年龄：')
    age = int(age)
    if age==30:
        print('恭喜！')
        break
    n = n+1


# 12.编写登陆接口   (已完成)
# 需求：
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序
# n =0
# while n < 3:
#     account = input('用户名：')
#     account1 ='lily'
#     password = input('密码：')
#     password1 ='123'
#     if account == account1 and password ==password1:
#         print('欢迎！')
#         break
#     else:
#         n = n+1

# 13.双色球选购游戏（已完成）
# 先让用户依次选择6个红球（红球的选择范围是1-32），再选择2个蓝球（篮球的选择范围是1-16），最后统一打印用户选择的球号。
# 确保用户不能选择重复的，选择的数不能超出范围（未处理）
# n = 0
# s1= ''
# while n<6:
#     num =input('请输入红球的号码：')
#     num1 = int(num)
#     if num1<=32 and num1>=1:
#         print('选择了红球：',num1)
#         s1 =s1+num+','       #字符串拼接
#         n=n+1
#     else:
#         print('请输入1-32的有效数字')
# m = 0
# s2= ''
# while m<2:
#     num0 = input('请输入蓝球号码：')
#     num2=int(num0)
#     if num2<=16 and num2>=1:
#         print('选择了蓝球',num2)
#         s2 =s2+num0+','     #字符串拼接
#         m =m+1
#     else:
#         print('请输入1-16的有效数字')
# print('您选择的红球号码为：',s1,'您选择的蓝球号码为：',s2)
