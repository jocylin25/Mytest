#反射：
#a.b====getattr(a,'b')
# import  sys
# print(getattr(sys.modules[__name__],'name'))   反射当前文件的变量
# print(getattr(sys.modules[__name__],'age'))
# getattr(sys.modules[__name__],'func')()          反射当前文件的方法
# print(getattr(sys.modules[__name__],'Student'))   反射当前文件的类

#1.对象的反射：
        #hasattr(对象，'属性名')  判断对象是否有这个属性，有返回True
        #getattr(对象，'属性名')  返回对象中属性名的对应值
    #反射属性
        #val=getattr(对象，'属性名')
        #val 就是属性的值
    #反射方法
        #val=getattr(对象，'方法名')
        #val就是方法的地址
        #val()调用方法
#2.类的反射
# class A:
#         role ='china'
# print(getattr(A,'role'))

#3.模块的反射
# import time
# print(time.time())
# print(getattr(time,'time')())

# class Student:
#     def __init__(self):
#         self.name ='alex'
#         self.age = 30
#         self.gender='male'
#
#     def show_info(self):
#         print('%s,%s'%(self.name,self.age))
# stu =Student()
# content =input('>>>')
# #判断调用方法还是调用属性
# if hasattr(stu,content):
#     name = getattr(stu,content)      #stu.show_info   name=show_info 的地址
#     if callable(name):                  #callable()  判断name是不是一个方法 是返回true 不是返回false
#         name()
#     else:
#         print(name)

#另一种方法：
# if content =='name':
#     print(stu.name)
# elif content =='age':
#     print(stu.age)
# elif content =='gender':
#     print(stu.gender)
#


#应用 选课系统
class Student:
    opt_lst =[('查看可选课程','show_courses'),('选择可选课程','choose_course'),('查看已选课程','show_selected_course'),('退出','quit')]
    def __init__(self,name):
        self.name =name
        self.courses=[]
    def show_courses(self):
        print('查看一共有多少门课程')
    def choose_course(self):
        print('选择课程')
    def show_selected_course(self):
        print('查看已经选择的课程')
    def quit(self):
        print('退出')

stu =Student('alex')
for index,opt in enumerate(Student.opt_lst,1):          #enumerate()是python 内置函数，遍历列表或字符串，将其组成一个索引序列，
# 利用它可同时获得索引和值。1：默认参数代表从1开始
    print(index,opt[0])
num =int(input('请输入需要选择的操作序号：'))
if hasattr(stu,Student.opt_lst[num-1][1]):
    print(getattr(stu,Student.opt_lst[num-1][1])())
