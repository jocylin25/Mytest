import hashlib
#md5码加密  32位
# md5 =hashlib.md5()
# md5.update (b'12345')
# ret =md5.hexdigest()
# print(ret)
#827ccb0eea8a706c4c34a16891f84e7b  32位 为12345 通过md5加密后的结果

#sha1码加密  加密后40位
# sha1 =hashlib.sha1()
# sha1.update (b'12345')
# ret1 =sha1.hexdigest()
# print(ret1)
#8cb2237d0679ca88db6464eac60da96345513964  为12345 通过sha1加密后的结果

#md5加字符串加密
# md5 =hashlib.md5(bytes('只有我知道别人不知道的字符串%s'%'alex',encoding='utf-8'))
# md5.update (b'12345')  #添加消息
# ret2 =md5.hexdigest()   #获得str类型消息摘要
# print(ret2)

#字符串被拆分加密与字符串加密的md5码一致
# md51 =hashlib.md5()
# md51.update ('你好中国'.encode('utf-8'))
# ret =md51.hexdigest()
# print(ret)
# md5 =hashlib.md5()
# md5.update ('你好'.encode('utf-8'))
# md5.update ('中国'.encode('utf-8'))
# ret1 =md5.hexdigest()
# print(ret1)

#文件加密
# import hashlib
# md5 =hashlib.md5()
# with  open(r'E:\python\data\project\StudyProject\day09\文件加密1.py','rb') as f:
#     content =f.read()
#     md5.update(content)
# ret =md5.hexdigest()
# print(ret)

#比较两个加密文件是否一致
# import hashlib
# def get_md5(file):
#     md5 =hashlib.md5()
#     with  open(file,'rb') as f:
#         content =f.read()
#         md5.update(content)
#     ret =md5.hexdigest()
#     return ret
# ret =get_md5(r'E:\python\data\project\StudyProject\day09\文件加密1.py')==get_md5(r'E:\python\data\project\StudyProject\day09\文件加密2.py')
# print(ret)