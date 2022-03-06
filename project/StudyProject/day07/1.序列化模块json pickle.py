#json模块
#json格式 {'key':'value'}   key必须是字符串，value只能是：字典 列表 字符串 数字 bool值
#json是所有编程语言通用的一种数据类型 ，type 是字符串
#网络传输、文件操作不能用字典
#loads dumps   和内存交互
#load dump     和文件交互
#json不支持多次dump pickle支持多次dump

#字典转换成json格式的字符串 序列化过程   字符串 =json.dumps(字典/列表)
#import json
# dic ={'username':'alex','password':'123'}
# ret =json.dumps(dic)     #文件操作时 加上 enumerate=False
# print(ret,type(ret))

# #字符串->字节 在网络传递
# byte1 =ret.encode('utf-8')
# print(byte1)
#
# #字节->字符串
# str1 =byte1.decode('utf-8')

# #json格式的字符串->字典   反序列化过程      字典/列表=json.loads(字符串)
# ret1 =json.loads(str1)
# print(ret1)

#写入文件
import json
# lst =['alex',1,2,3]
# with open('file',mode='w',encoding='utf-8') as f:
#     ret =json.dump(lst,f)
#读文件
# import json
# with open('file',mode='r',encoding='utf-8') as f:
#    ret =json.load(f)
#    print(ret)


#pickle 模块(只有python中有,几乎支持所有数据类型)
# import pickle
# dic ={'北京':{'朝阳','昌平'},('alex','david'):[1,2,3]}
# ret=pickle.dumps(dic)
# print(ret)
# d =pickle.loads(ret)
# print(d)

#写入文件
# with open('pickle_file','wb') as f:
#     pickle.dump(dic,f)
#读文件
# with open('pickle_file','rb') as f:
#     ret =pickle.load(f)    #ret为字典
# print(ret.__dict__)   #读取字典
#     print(ret)
#     print(ret.北京)