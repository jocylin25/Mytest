#三大特性：封装  继承  多态
#封装：
    # 广义把方法和变量名封装在类中，类的外部不能直接调用了
    # 狭义上
    #私有化  ：属性名、类变量、方法名前加上双下划线 __ ，私有化后只能在类的内部使用，外部不能通过变量名调用了
    #私有化原理：只是在类内部使用的时候对名字进行包装，变成 _类名***
# class student():
#     __val=[]     #私有化类变量
#     def __init__(self,name):
#         self.__name=name    #私有化属性
#     def __a(self):        # 私有化方法
#         print('aa')
# alex =student('alex')
#私有化后外部不能通过变量名调用了
#print(alex.name)
#print(alex.__name)
#print(alex.val)
#print(alex.__a())

#私有的不能被继承
# class A:
#     def __func(self):    #_A__func
#         print('in a')
# class B(A):
#     def __wahaha(self):
#         self.__func()          #_B__func
#
# b =B()
#练习题
# class A:
#     def __init__(self):
#         self.__func()         #self._A__func
#     def __func(self):       #_A__func
#         print('in a')
# class B(A):
#      def __func(self):  # _B__func
#         print('in b')
# b =B()

#多态 ：一个类被多个子类继承
#装饰器
    # @property  @classmethod @classmethod

# class User:pass
# class Student(User):
#     def __init__(self,name,birth):
#         self.name =name
#         self.birth =birth
#     @property           #将一个方法伪装成属性
#     def age(self):
#         import time
#         return time.localtime().tm_year - self.birth
# class Manager(User):pass
# def change_pwd(User,person): #学生对象管理员对象都能传进来
#     pass
#
# alex =Student('alex',1930)
# print(alex.age)   #名词调用方法

#实例方法  静态方法  类方法
# class A:
#     def func1(self):pass       #实例方法:self 作为默认参数，通过对象来调用
#     @classmethod
#     def func2(cls):pass        #类方法：cls作为默认参数，可以用类名调用
#     @staticmethod
#     def func3():pass        #静态方法 没有默认参数，可以用类名调用
#
#
# class Student:
#     def __init__(self,name):
#         self.name =name
#
#     @staticmethod           #静态方法：不必传任何默认的参数，不用实例化，不用通过对象调用,可直接通过类名调用
#     def login():
#         print('登陆')
#     @classmethod          #类方法，默认传参数cls，表示当前所在的类名，可直接通过类名调用
#     def exit(cls):
#         username=input('>>>')
#         stu =cls(username)
#         return stu
#
# Student.login()
# obj =Student.exit()
# print(obj.__dict__)    #  __dict__:内置方法查看值

#双下方法（内置方法）
    #__str__（）： 打印这个方法的返回值
    #__new__（）：构造方法  创建一块内存空间  构造对象的方法
# class Course:
#     course_lst =[]
#     def __init__(self,name,period,price):
#         self.name =name
#         self.period =period
#         self.price=price
#     def __str__(self):                #__str__返回这个方法的返回值
#         return '%s%s%s'%(self.name,self.period,self.price)
# python =Course('python','6 months',19800)
# linux =Course('linux','5 months',17800)
# Course.course_lst =[python,linux]
# for course in Course.course_lst:
#     print(course)    #print（obj）打印一个对象总是打印内存地址，通过obj.__str__回这个方法的返回值


#单例模式：无论实例化多少个，最新的实例化都会覆盖之前的值
#单例模式怎么实现？
#先通过__new__()创建一个内存空间，再调用__init__()初始化方法
#单例模式例子：
# class Singleton:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             obj =object.__new__(cls)    #创建内存空间
#             cls.__instance =obj
#         return cls.__instance
#     def __init__(self,name):
#         self.name =name
# obj1=Singleton('alex')       #先调用 __new__ 再调用__init__
# obj2=Singleton('david')
# print(obj1.name,obj2.name)



