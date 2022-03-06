#圆形类
#属性 半径
#内部提供两个方法  计算周长 2Πr  计算面积Πr**2
from math import pi
class Circle:
    def __init__(self,r):
        self.r=r
    def perimeter(self):
        return 2*pi*self.r
        print('周长为%s'%per)
    def area(self):
        return pi*self.r**2
        print('面积为%s'%s)

a1=Circle(9)
a1.perimeter()
a1.area()

class Ring:
    def __init__(self,outer_r,inner_r):
        c1 =Circle(outer_r)
        c2=Circle(inner_r)
        self.outer =c1        #如果一个属性和一个对象联系在一起叫做 组合
        self.inner =c2
        def area(self):
            return self.outer.area()-self.inner.area()
        def perimeter(self):
            return self.outer.perimeter()+self.inner.perimeter()