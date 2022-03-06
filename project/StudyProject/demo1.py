#单选
# 1.Python语句如何将数字转换为字符串 A
# A.str() B.int() C.float（）D.list（）

# 2.启动浏览器的时候用到的是哪个webdriver协议？A
# A.HTTP B.DHCP C.RARP D.TFTP

# 3.page object设计模式中，如何实现页面的跳转？B
# A.clear方法 B.click方法 C.input方法 D.get方法

# 4.L = [1, 2, 3, 4, 5]，L[10:]的结果是？ D
# A.[1, 2, 5] B.[1, 4, 5] C.[2, 3, 4, 5] D.空列表[]

# 5.L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]，用一行代码得出 [11, 1, 2, 3, 5]  A
# A.list(set(L)) B.str(set(L)) C.group(set(L)) D.sub(set(L))

# 6.如何用 webdriver 进行鼠标右键点击操作?   D
# A.使用 Chains 类 B.使用ClickChains 类 C.使用 ActionsDo 类 D.使用 ActionChains 类

# 7.查看变量类型的 python 内置函数是   C
# A.by（）B.list（）C.type（）D.get（）

# 8.单元测试框架，有哪些常用注解      A
# A.BeforeClass B.Claas C.Beforer D.Beforeas

# 9.写出语句打印" let's go", she said    B print("\""\,she said")
# A.print("\"let's go\"!she said")
# B.print("\"let's go\",she said")
# C.print(let's go\",she said")
# D.put("\"let's go\",she said")

# 10.怎么获得当前页面的URL? A
# A.String url = driver.getCurrentUrl();
# B.String url = set.getCurrentUrl();
# C.Strings url = driver.putCurrentUrl();
# D.String url : driver.getCurrentUrl();

#多选
# 1.Selenium定位不到元素如何处理   ABCD
# A.sleep
# B.观察页面 页面有有没有跳转，元素有没有出现，有没有弹出alert
# C.元素是否在框架里
# D.元素是否在新页面里
# 2.如何提高selenium脚本的执行速度？ABD
# A.少用sleep
# B.多用显式等待方法
# C.多用复杂方法
# D.弄个性能好的电脑
# 3.下面哪些关于自动化测试的说法是错误的 ABCD
# A.自动化测试可以完全取代手工测试
# B.自动化测试可以大幅度减少测试团队的工作量
# C.性能测试不能自动化
# D.自动化测试能够发现大量的新缺陷
# 4.Python 中自定义的函数如何传递动态参数?CD
# A.*wargs
# B.*Bwargs
# C.*args
# D.*kwargs

#填空
# 1.自动化测试用[$##$]校验结果     断言assert
# 2.阅读代码，请写出执行结果
# def res_max(number1,number2):
#     l1 = [$##$]
#     l1.append(number1)
#     l1.append(number2)
#     return max(l1)
# number1=10,number2=20
# 请写出输出结果: 20

# #问答
# 1.如何去定位属性动态变化的元素？ 先去找该元素不变的属性。要是都变，那就找不变的父元素，用层级定位（以不变应万变）
# 2.用Python写一个函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
# 例如：
# 传入1：[34,23,52,352,666,3523,5] 返回1：[34,23,52,352,666]
# 传入2：[34,23,52] 返回2：[34,23,52]
# def judlen():
#     str =input("请输入列表：")
#     list=eval(str)
#     if len(list)>5:
#         list1 =list[0:5]
#         return list1
#     else:return list
# value =judlen()
# print(value)

