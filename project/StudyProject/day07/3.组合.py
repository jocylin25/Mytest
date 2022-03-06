#学生 姓名年龄 所学习的课程
class Student:
    def __init__(self,name,sex,age,course):
        self.name=name
        self.sex=sex
        self.age=age
        self.course=course
class Course:
    def __init__(self,cname,period,price):
        self.name=cname
        self.period=period
        self.price=price

python =Course('python','6 months',19800)
php =Course('php','2 months',18800)
a =Student('alex','女','23',python)
a.course =php
print(python.price)
python.price =21000
print(a.course.price)
