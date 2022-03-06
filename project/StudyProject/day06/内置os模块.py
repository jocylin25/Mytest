#内置模块
#re模块:正则表达式用
#时间模块
    #time模块：操作时间
    #datetime
#os模块:和操作系统打交道，与操作系统交互的一个接口
    #文件夹操作、
        #1.创建多层递归目录：os.makedirs('dirname1/dirname2')
        #2.删除多级目录 ：os.removedirs('dirname1')          目录为空则删除，递归到上一级目录，若为空也删除,目录不为空报错
        #3.删除单级空目录：os.rmdir('dirname')      目录为空则删除,目录不为空报错
        #4.创建单级目录：os.mkdir('dirname')
        #5.os.listdir('dirname')           列出指定目录下所有文件和子目录，并以列表方式打印
    # 文件操作、
        #1.删除文件：os.remove()
        #2.重命名文件/目录：os.rename("old","new")
        #3.获取文件/目录信息 os.stat('path/filename')
    # 执行操作系统命令、
        #1.os.system('shell command') 直接显示
        #2.os.popen('shell command').read()  获取执行结果
        #3.os.getcwd()   获取当前目录
    # 更改工作目录
        #.os.chdir("dirname") 进到指定工作目录，相等于cd
    #os.path
    #os.path.getsize(绝对路径)   获取文件的大小，但不能获取文件夹的准确大小
    #os.path.isfile(绝对路径)    判断是否是文件
    #os.path.isdir(绝对路径)       判断是否是文件夹
    #os.path.join(文件夹的名字，名字)     跨平台拼接文件路径和文件名
    #os.listdir('文件夹的路径')    显示这个文件夹下的所有名字
    #os.path.exists(path)    path存在返回true，不存在返回false
    #os.path.isabs(path)   判断path是否是绝对路径
    #os.path.isfile(path)  判断path是否是存在的文件
    #os.path.isdir(path)   判断path是否是存在的目录
    #os.path.getatime(path) 返回path的最后访问时间
    #os.path.getmtime(path) 返回path的最后修改时间
    #os.path.getmtime(path) 返回path的最后修改时间
    #os.path,abspath(path)  返回规范化绝对路径
    #os.path.split(path)   path分割成目录和文件名二元组
    #os.path.dirname(path) 返回path目录
    #os.path.basename(path)   返回path文件名  若path以\结尾 则返回空值

#练习：计算文件夹大小
#循环的方式实现：
import os
# def dir_size(path):
#     if os.path.isdir:
#         sum_size =0
#         dirs=[]
#         dirs.append(path)      #dirs=[path]
#         while dirs:
#             path =dirs.pop()   #移除列表中最后一个元素并返回这个元素的值  此时dirs=[]
#             dir_lst =os.listdir(path)
#             for name in  dir_lst:
#                 file_path =os.path.join(path,name)
#                 if os.path.isfile(file_path):
#                     sum_size +=os.path.getsize(file_path)
#                 else:
#                     dirs.append(file_path)
#         return sum_size
#     elif os.path.isfile(path):
#         return os.path.getsize(path)
#     else:
#         print('找不到文件')
# path =r'E:\python\data\project\StudyProject\day06'
# ret =dir_size(path)
# print(ret)

#sys模块：和python解释器相关
#序列化模块：  json  pickle
#logging模块：打印日志用，规范日志格式
#hashlib模块：摘要算法的集合-密文的登录验证
