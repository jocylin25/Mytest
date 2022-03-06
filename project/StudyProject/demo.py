#单选题 27
#1.用边界值分析法，假定1<X<100，那么X在测试中应该取的边界值是  A
#A.X=1，X=100；B.X=0，X=1，X=100，X=101； C.X=2，X=99 D. D．X=O，X=101；
# 2.Selenium自动化测试为哪类 A
# A.UI自动化 B. 终端自动化 C. 数控自动化  D.安全自动化
# 3.Linux  的常用命令  B
# A.du  B.ls C.ns D. mkdit
# 4.你如何验证多个页面上存在的一个对象  C
# A.assertBTrue  B. assertNOTrue C. assertTrue D.以上答案都不对
# 5.你如何清除中文本框的内容？  A
# A.clear（）方法。B.input（）方法。C.sendkeys（）方法。D.click（）方法。
# 6.下列哪个语句在Python中是非法的？  B
# A.x = y = z =1  B.x = (y = z + 1) C.x, y = y, x D.x  +=  y

# 7.下面哪个不是Python合法的标识符 B
# A.int32 B.40XL  C.self D.name
# 8.Python不支持的数据类型有 A
# A. charB.int C.float D.list
# 9.下列Python语句正确的是： D
# A.min = x if x< y = y
# B.max = x > y ?x:y
# C.if (x >y)   print x
# D.while True :pass
# 10.下列哪种说法是错误的  A
# A.除字典类型外，所有标准对象均可以用于布尔测试
# B.空字符串的布尔值是False
# C.空列表对象的布尔值是False
# D.值为0的任何数字对象的布尔值是False
# a ={}
# print(bool(a))
# #多选题 10
# 1.在selenium自动化测试中，你一般完成什么类型的测试？AB
# A.冒烟测试
# B.回归测试
# C.全量测试
# D.复杂场景测试
# 2.如何去定位属性动态变化的元素？ BC
# A.names名字
# B.xpath通过同级、父级、子级进行定位
# C.css通过同级、父级、子级进行定位
# D.id通过编号
# 3.你觉得自动化测试最大的缺陷是什么？ ABCD
# A.不稳定
# B.可靠性
# C.不易维护
# D.成本与收益
# 4.Pyhton 注释用什么？ AB
# A.# B."""   """C. ‘’D.//

#填空题10
#1.用___方法实现文件上传。  sendKeys
#2.阅读代码，请写出执行结果
# a = “alex”
# b=a.capitalize()
# print(a)
# print(b)
# 请写出输出结果: alex Alex
#问答题
#1.用___方法实现文件上传。 sendKeys方法加文件路径
#2.
import copy
list1 = [1,2,['a','b'],('c','d')]
list2 = list1               #[1,2,['a','b',{100},{'1'：1111}],('c','d',10,10),3]
list3 = copy.copy(list1)     #[1,2,['a','b',{100},{'1'：1111}],('c','d')]
list4 = copy.deepcopy(list1)     #[1,2,['a','b'],('c','d')]
list1.append(3)        #
tuple1 = (10,10)
list1[2].append({100})
list1[3] = list1[3] + tuple1
dict1 = {}
dict1['1'] = 1111         #dict={'1':1111}
list1[2].append(dict1)
print(list1)   #[1,2,['a','b',{100},{'1':1111}],('c','d',10,10),3]
print(list2)   #[1,2,['a','b',{100},{'1':1111}],('c','d',10,10),3]
print(list3)   #[1,2,['a','b',{100},{'1':1111}],('c','d')]
print(list4)   #[1,2,['a','b'],('c','d')]
