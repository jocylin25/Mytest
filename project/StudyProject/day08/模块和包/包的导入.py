#第一种方式
# import pack.api.policy as policy
# print(policy.name)
#第二种方式
# from pack.api import policy
# print(policy.name)

import sys
#print(sys.path)
#将被导入模块或包所在的路径加入sys.path列表中
sys.path.append('E:\\python\\data\\project\\StudyProject\\day08\\模块和包')
from pack.api import policy
print(policy.name)