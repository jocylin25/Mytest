#py3.X所有类都是object子类 即新式类   遵循是广度优先 C3算法
#Objectl类中写了一些内置方法，如果子类不定义，调用的时候就会调用object类中的方法，如__init__
#py2 新式类 ：
            # 所有继承了object类    class A(object):pass
#    经典类：
            # 不继承object的类   class A:pass
            # 在多继承中遵循深度优先
            # 没有super和mro方法
