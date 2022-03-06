__author__ = 'admin'
#正则表达式：只针对字符串，匹配字符串的一种规则
    #1.从一大段文字中，获取符合条件的内容
        #爬虫
    #2.检测某一个字符串中，是否完全符合规则
        #表单的验证：根据一些规则先判断是否合法
    #常用正则表达式：
        #字符组
            #[0-9]:匹配所有数字
            #[a-z]:匹配所有小写字母
            #[A-Z]:匹配所有大写字母
            #[0-9a-zA-Z]:匹配所有字母数字
            #一次取多个区间：只能从ascii码小的值到大的值[0-9a-f]
        #元字符
            #\d    [0-9]
            #\w   [0-9a-zA-Z]
            #\s \t  \n   匹配所有的空白符\制表符\换行符
            #\D  \W \S   匹配所有的非数字\匹配所有的非数字字母下划线\匹配所有的非空白
            #空格：      匹配空格
            # .         匹配除了换行符之外的任意一个字符
            #^  $       匹配以。。开始   匹配以。。结束
            #[]  [^]     字符组  非字符组
            #|            或
            #()       规范符号的作用
            #只写元字符 一个元字符表示一位字符上的内容
        #量词
            #{n}       表示匹配n次
            #{n,}      表示匹配至少n次
            #{n,m}     表示匹配n-m次
            #?         0或1次
            #+         1-无穷大
            #*         0-无穷大
            #元字符量词 量词只约束前面的一个元字符\
            #（元字符元字符）量词约束括号里的所有元字符
        #转义符
            #所有的特殊字符都需要转义才能恢复本来的意思
            #匹配手机号：1[3-9]\d{9}
            #匹配任意的正整数[1-9]\d*
            #匹配任意的小数\d+\.\d+
            #匹配整数或小数\d+(\.\d+)?
        #贪婪和惰性
            #贪婪匹配   a .*b：在符合条件的基础上尽量多的匹配内容
            #惰性匹配  量词后面的？表示惰性匹配，会在符合条件的基础上尽量少的匹配内容

#re模块：操作正则表达式
import re

#1.re.findall('正则表达式','字符串')  匹配所有匹配项
#返回值：列表，所有匹配到的项都会被返回到列表中
# ret1 = re.findall('\d+','hello123,world456')
#？：取消分组优先
# ret3 = re.findall('\d+(?:\.\d+)?','hello123.178,world456.234')
# print(ret3)

#2.re.search('正则表达式','字符串')  只匹配从左到右第一个匹配项

# ret2 = #返回值：re自定义类型re.search('\d+','hello123,world456')  #返回变量
# ret2.group()    #取从左到右第一个匹配项
#例题：手机号长度验证
# phone_num =input('请输入合法的手机号')
# regex =r'^1[2-9]\d{9}$'
# ret =re.search(regex,phone_num)
# if ret:
#     print('%s是合法的手机号'%phone_num)
# else:
#     print('%s手机号不合法'%phone_num)


#3.search取分组中的内容：根据序号取，根据组名取 命名组：P<组名>
#返回值：re自定义类型
# ret =re.search('(?P<num1>\d)(?P<num2>\d)','b28,a1,c234')
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group('num1'))
# print(ret.group('num2'))
#分组的引用:?P=num1表示引用了num1的分组，匹配到的内容必须和num1分组中的内容一摸一样
# ret=re.search('(?P<num1>\d)(?P=num1)','a14,b22,c345')
# print(ret.group())


#4.re.match('正则表达式','字符串')
#匹配用户输入的内容是否合法时都用match
#功能：从头开始匹配，开头匹配一致成功，开头匹配不一致失败
#返回值：re自定义类型
#search 的r'^1[2-9]\d{9}$' 同match r'1[2-9]\d{9}$'作用
# phone_num =input('请输入手机号')
# regex =r'1[2-9]\d{9}$'
# ret =re.match(regex,phone_num)
# if ret:
#     print('%s是合法的手机号'%phone_num)
# else:
#     print('%s手机号不合法'%phone_num)

#5.finditer   返回一个匹配的迭代器，循环通过group取值未存在内存里，节省空间
# ret =re.finditer('\d','alex87654310')
# for i in ret:
#     print(i.group())

# 6.compile 预编译  ，预先编译写好的正则 节省时间成本
# rule =re.compile('\d+')
# ret=rule.findall('exca9888999888')
# ret=rule.findall('手机号13567677788')

#7.split 根据正则做切割
# ret =re.split(r'\d+',r'alex84wusir33')
# print(ret)
#8.sub  替换方法1（正则表达式，替换的内容，待替换的字符串，替换的个数）
# ret =re.sub(r'\d+','H','eva123alex666',2)
# print(ret)
#9.subn  替换方法2（正则表达式，替换的内容，待替换的字符串)  返回值是一个元组：第一项结果，第二项替换个数
# ret =re.subn(r'\d+','H','eva123alex666')
# print(ret)


#练习题：re模块和正则表达式 循环
#exp ='1 - 2*((60-30+(-40/5)*(9-2*5/3 + 7 /3*99/4*2998 +10 *568/14))-(-4*3)/(16-3*2))'
