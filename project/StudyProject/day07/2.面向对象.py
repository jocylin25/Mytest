# def Dog(name,kind,sex):
#     dog_dic={'name':name,'kind':kind,'sex':sex}
#     return dog_dic
#
# dog1=Dog('小白','哈士奇','公')
# dog2=Dog('小黑','泰迪','母')
# print(dog1)
# print(dog2)

#面向对象：属性技能放在角色模板里 --可扩展性高
#类：class  一系列具有相同属性和方法的事物的抽象
#对象：一个带有具体属性值的类的实例
#实例化：通过类创建对象的过程
#类名作用：
            # 1.可以调用类中的变量  Dog.discount
            #2.实例化创建对象   Dog('小白','哈士奇','公')
            #3.调用方法      类名.方法名()
#对象名作用：
    #查看对象的属性      对象名.属性
    #调用对象的方法      对象名.方法名()

#命名空间
#class A：
#   静态变量='值'
#   def __init__(self,属性）：
#       self.属性名 =属性
#       def show(self):
#           print('展示所有的属性')
#a=A('参数')    #对象a
#print(a.静态变量)    #对象可以引用类的命名空间中的内容包括方法和静态变量
#类的命名空间中
    # 静态变量
    # 方法

#对象的命名空间中
    # 对象指针
    #实例变量/对象的属性
    #用对象修改局部变量只要用到赋值，相当于在自己空间中新建

#__dict__ 内置属性 查看类或者对象的命名空间存储了什么
#操作静态变量
#如果是查看 用类和对象都可以
#如果是修改，只用类名进行修改
#不要在对象的空间中创建一个和类变量同名的实例变量

#例子：class类名：创建一个类
class  Dog:                             #Dog类：
    discount = 5          #类变量 静态变量
    def __init__(self,name,kind,sex):            #__init__(self) 初始化方法  实例方法
        self.dname=name                   #实例变量
        self.dkind=kind
        self.dsex=sex
    def bite(self):           #self 为dog1
        #谁在外部调用了这个方法，方法中的第一个self参数就是谁
        print('被调的参数为%s'%self.dname)

dog1 =Dog('小白','哈士奇','公')      #dog1对象   实例化
# print(dog1.dname)
# print(dog1.dkind)
# print(dog1.dsex)
dog1.bite()                  #同Dog.bite(dog1)