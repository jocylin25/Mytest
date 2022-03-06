#A和B类都需要调用相同的方法
#创建父类C，把相同的方法放到C类
#A和B继承C A（C） B（C）
#A的对象和B的对象可以直接调用C中方法
#自己有还想调用父类的方法：在子类中直接调用父类的方法
class Animal:
    def __init__(self,hp,ad,name):
        self.hp =hp
        self,ad=ad
        self.name=name

class Dog(Animal):   #继承父类
    def __init__(self,hp,ad,name,sex,job):
        self.sex =sex    #子类特有属性
        self.job=job        #子类特有属性
        Animal.__init__(self,hp,ad,name)   #引用父类方法
#继承
    #super
    #单继承的作用就是找父类
    #多继承是找mro顺序的下一类
    #查看多继承中的继承顺序   #A.mro()

# class Course:
#     course_lst =[]
#     def __init__(self,name,period,price):
#         self.name =name
#         self.period =period
#         self.price=price
# class Role:
#     def __init__(self,name):
#         self.name =name
#     def show_course(self):
#         for item in Course.course_lst:
#              print(item.name,item.period,item.price)
#
# class Student(Role):
#     def __init__(self,name):
#        #Role.__init__(self,name)
#        #super(Student,self).__init__(name)
#         super().__init__(name)       #super可以帮助我们找到父类
#         self.courses_lst =[]
# class Manager(Role):  pass
#
# python =Course('python','6 months',19800)
# linux =Course('linux','5 months',17800)
# Course.course_lst =[python,linux]          #所有的可选课程
#
# m =Student('alex')
# print(m.name)
# m.show_course()


#多继承：
# class D:
#     def func(self):
#         print('D')
# class C(D):
#     def func(self):
#         super().func()
#         print('c')
# class B(D):
#     def func(self):
#         super().func()
#         print('B')
# class A(B,C):
#     def func(self):
#         super().func()
#         print('A')
# a =A()
# a.func()
# print(A.mro())   #查看A  mro继承顺序