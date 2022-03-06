__author__ = 'admin'
#例题：创建一个有100件衣服的列表
#生成器函数  没有return，只有yield,generator生成器的本质就是一个迭代器
# def cloth(n):
#     for i in range(n):
#         yield'第%s件衣服'%i
#
# ret = cloth(100)
# for i in range(5):   #100件衣服取前5件衣服
#     print(ret.__next__())

#练习题：监听文件的输入，在python中监听一个文件的输入事件，只要用户输入新内容，就打印到屏幕中央
# while True:
#     f =open('test','a',encoding='utf=8')
#     content =input('>>>')
#     f.write()
#     f.close()
#监听文件生成器
# def listen():
#     f =open('test',mode='r',encoding='utf-8')
#     while True:
#         content =f.readline().strip()
#         if 'error' in content:
#             yield content
# for content in listen():
#     print(content)

#登陆读文件，注册检测是不是存在相同的用户名，读文件操作写成一个生成器
#所有读文件写文件尽量拆分不同函数，不要嵌入到功能函数

#生成器函数：读、写文件逻辑
def get_user(file):
    with open(file,mode='r',encoding='utf-8')as f:
        for line in f:
            usr,pwd =line.strip().split('|')
            yield usr,pwd
#登陆
def login():
    user =input('用户名：')
    password = input('密码：')
    for usr,pwd in get_user('test'):
        if user ==usr and password==pwd:
            print('登陆成功')
            break
    else:
        print('登陆失败')

login()

