__author__ = 'admin'
#模块分类：
    #内置模块：不需要自己安装，直接就可以使用
    #扩展模块/第三方模块：需要自己安装一下才能使用 django flask beautifulsoup pandas等
    #自定义模块

#内置模块
#random模块：操作随机数
#random  生成或处理随机数
# 随机
# 随机规则：在某一个范围中能够抽到每一个值的概率都相同
import random
#1.random.random()           生成(0,1)之间随机数
# random.random()
#2.random.randint(a,b)           生成[a,b]之间随机整数
#random.randint(a,b)

#3.random.randrange(a,b,n)         [a,b)之间隔n个生成一个随机整数
# ret =random.randrange(1,20,2)
# print(ret)

#4.random.shuffle(lst) 洗牌
# lst =[1,2,3,4,5]
# random.shuffle(lst)
# print(lst)

#5.random.choice(lst)从列表中随机抽取一个
# ret = random.choice([1,2,'alex',[1,2,3]])
# print(ret)

#6.random.sample(lst,k)从列表中随机抽取k个
# ret =random.sample([1,2,'alex',[1,2,3]],2)
# print(ret)

#作业：random实现一个验证码，可以是4位或6位，纯数字或数字+字母
