# coding=gbk
# 1.��100���ڵ������ͣ�����1�ͱ����ܱ�������������
# sum = 0
# for i in range(2,101):
#     for j in range(2,i//2+1):
#         if i%j ==0:
#             break
#     else:
#         print(i)
#         sum +=i
# else:
#     print('������Ϊ%s'%sum)

#�ļ�����
#��
# f =open(r'E:\python\data\project\StudyProject\day03\userinfo',
#         mode ='r',
#         encoding='utf-8')
# print(f.read())
# f.close()
#д
# f =open(r'E:\python\data\project\StudyProject\day03\userinfo',
#         mode ='w',
#         encoding='gbk')
# f.write('\nС�֣�27')
# f.close()
# f =open(r'E:\python\data\project\StudyProject\day03\userinfo',
#         mode ='a',
#         encoding='gbk')
# f.write('\nС�֣�26')
# f.close()

#����
# lst =[1,2,3,4]
# #�����Ķ���
# def mylen():
#         i = 0
#         for j in lst:
#                 i+= 1
#         print(i)
# #�����ĵ���
# mylen()

#��ϰ��1 д������a b c ����ֵ������a*b/c�Ľ������ӡ
# a =1
# b =2
# c =3
# def abc():
#         s = a*b/c
#         return s           #����ֵ
# ret = abc()
# print(ret)
#
# def sum(a,b,c):  #��ʽ����
#     return a+b+c
# ret =sum(1,2,3)     #ʵ��
# print(ret)
#��ϰ��2 д���������������������Ƚ����������Ĵ�С�������ؽϴ����һ����ֵ
# def ab(a,b):
#     if a>b:
#         return a
#     else:return b
# a = input('����a��ֵ')
# b = input('����b��ֵ')
# v =ab(int(a),int(b))
# print(v)

#��ϰ3 �б�/Ԫ��/�ַ���/�ֵ� ���������͵ĳ��ȱȣ��������ݳ��ȸ���������
# def mylen(seq):
#     i =0
#     for j in seq:
#         i +=1
#     return i
# def compare(seq1,seq2):
#     if mylen(seq1)>mylen(seq2):
#         return seq1
#     else:
#         return seq2

#�ֲ��޸�ȫ�ֱ���
# a =1
# def func():
#     global a
#     a +=1
#     print(a)
# func()

#�߽׺���
# f=1
# def outer():
#     f=2
#     def inner():
#         nonlocal f
#         f =f+1
#         print('inner',f)
#     inner()
#     print('outer',f)
# print('ȫ��',1)
# outer()