import  sys
#1.sys.modules
#输出当前执行代码的位置，解释器中导入的所有模块被放到字典里
#字典的key就是模块的名字，对应的value是这个模块对应的内存中位置
#import time == sys.modules['time']
#print(sys.modules)

#2.sys.path
#(1)导入模块时，这个模块所在的路径在sys.path中才能导入
#(2)在sys.path中寻找数据时，能够找到一个文件就不继续往下走了
#(3).pycharm会自动把当前项目路径添加到sys.path中，实际生产环境不出现这个值
#print(sys.path)

#3.sys.argv  执行当前文件的时候可传递一些参数
#sys.argv[1] =='alex'
#print(sys.argv)