__author__ = 'admin'
#一.time模块
import time
#1.时间戳时间
# time.time()
#2.结构化时间  tm_isdst:是否夏令时
# time.localtime()
#3.格式化时间  （字符串时间）  不支持中文
# time.strftime('%Y-%m-%d %H:%M:%S')

#格式之间转化
#1.时间戳->结构化时间
#time.localtime(时间戳)        #北京时间
#print(time.localtime(15000000000))
#time.gmtime(时间戳)         #UTC时间
#print(time.gmtime(15000000000))
#2.结构化时间->时间戳
#time.mktime(结构化时间)
# time_tuple =time.localtime(15000000000)
# print(time.mktime(time_tuple))
#3.格式化时间->结构化时间
#time.strptime(时间字符串，字符串对应格式)
# s =time.strptime('2019-08-23','%Y-%m-%d')
# print(s)
#4.结构化时间->格式化时间
#time.strftime("格式定义","结构化时间")
# g =time.strftime('%Y-%m-%d',time.localtime(15000000000))
# print(g)

#二.datetime模块
from datetime import datetime
#datetime.now() 获取当前datetime
#datetime.utcnow() 获取当前格林威治时间
#创造时间
# dt =datetime(2019,10,11,12,10)
# print(dt)
#字符串转化成时间
# s1 ='2021/9/30'
# s2 ='2021年9月30日星期六'
# s3 ='2021年9月30日星期六7时20分30秒'
# s4 ='9/30/2021'
# s4 ='9/30/2021 7:20:30'
# ret = datetime.strptime(s1,'%Y/%m/%d')
# print(ret)
#时间转化成字符串
# dt =datetime(2019,8,11,17,8)
# str=dt.strftime('%Y-%m-%d %H:%M:%S')
# print(str)
#时间差
# dt1 =datetime(2019,8,11,17,8)
# dt2 =datetime(2020,8,11,18,8)
# res =dt2 -dt1
# print(res.seconds)     #相差多少秒
# print(res.days)        #相差多少天
# print(res.total_seconds()) #包括天数相差多少秒

#三.练习题：求当前月的1号对应的0点的时间戳时间
