# import requests
# import  json
#2.实现一个get请求的测试效果
# url ='http://127.0.0.1:5000/api/demo'
# data ={
#     'limit':1
# }
# #获得状态码
# res =requests.get(url=url,params=data)
# print(res)
# #获得响应body
# print(res.content)
# #获取解析后响应body
# print(res.text)

#3.实现一个post请求的测试效果
# res =requests.post(url=url,data=data)

#4.登陆接口测试例子
# url ='http://127.0.0.1:5000/api/login'
# #接口规则定义
# headers ={
#     'Content-Type':'application/json'
# }
# data ={
#     'username':'admin',
#     'password':'123456'
# }
# data_json=json.dumps(data) #字典转化成json格式
# #获得状态码
# res =requests.get(url=url,headers=headers,data=data_json)
# # #获取解析后响应body
# # print(res.text)
#
# # 断言校验
# text =json.loads(res.text) #字符串转json
# print(text['msg'])    #提取响应内容的msg
# #断言响应内容是否一致
# assert 'success'==text['msg'],'登陆失败'

#requests二次封装类与关键字驱动

from api_keyword.keyword_demo import KeyDemo
#引入config
import configparser
#导入包读取yaml文件
import yaml

conf =configparser.ConfigParser()
kd =KeyDemo()
#获取yaml文件数据内容
file =open('../data/login.yaml','r')
data =yaml.load(file,yaml.FullLoader)   #yaml.load(file对象,yaml.FullLoader) 通过yaml读取文件
print(data)
#测试数据
conf.read('../config/config.ini')
#获取config中url
url =conf.get('DEFAULT','url')+ data['path']
#执行测试
res =kd.post(url=url,data=data['data'])
print(res.text)