__author__ = 'admin'
# coding=gbk
#��ʽ�����
# name = input('������')
# print('welcome %s'%name)
# print('welcome %s'%20)
# print('welcome %d'%20)

#�б�
# lst = ['��','Ǯ','��','��']
# print(lst)
#����
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[-1])     #���һ��Ԫ��
# print(lst[-2])     #�����ڶ���Ԫ��
# print(lst[-3])
# print(lst[-4])

#��Ƭ
# print(lst[:])          #ȫ��Ԫ��
# print(lst[:2])         #��0��Ԫ���е���2��Ԫ��֮ǰ
# print(lst[2:])         #�ӵ�2��Ԫ�ؿ�ȡ
# print(lst[1:2])        #ȡ��ȡ��
# print(lst[-3:-1])       #������3��ȡ��������2��Ԫ��  ʡ��1��step
# print(lst[-3:-1:1])     #������3��ȡ��������2��Ԫ��  1��step
# print(lst[-1:-3:-1])    #�ӵ�����1��ȡ��������2��Ԫ��   -1��step
# print(lst[-1:-3])       #����-1��step����ʡ��
# print(lst[::2])         #�ӵ�0��Ԫ�ظ�����ȡ
# print(lst[::-1])        #�б�ת

#�б�Ŀ���
# lst2 = lst[:]
# lst3 = lst[::]
# lst4 = lst.copy()

#����Ԫ��
#lst.append('������')
#ɾ��Ԫ��
#
#��ϰ1������һ���˵�������������
# name = input('name:')
# password = input('password:')
# year = input('year:')
# lst5 =[]
# lst5.append(name)
# lst5.append(password)
# lst5.append(year)
# print(lst5)

#ֵ������
#�б�ǳ����  �ڴ��ַ����
# l =[1,2,['linda','25'],'3']
# print(len(l))
# for n in l:
#     print(n)
# l1 = l[:]
# l2 = l.copy()
# l2[2].append('hellokitty')
# print(l)
# print(l1)
# print(l2)

#���  �ڴ��ַȫ������һ�� �����˷��ڴ治����
# import copy
# l2 = copy.deepcopy(l)
# l2[2].append('hellokitty')
# print(l)
# print(l2)

#�鿴����λ��
# l.index('��������')

#enumerate ���������б��е�Ԫ��Ԫ�黯,����б�Ԫ�غ����
lst  = ['alex','eric','rain','linda','david','wind']
print(list(enumerate(lst)))

#ͨ�ò���
    # in  not in �ж�һ��Ԫ���ڲ����б���

#��ϰ2��
# ѭ��3��
# �����û�������������ʾ���Ѿ����� δ���ڣ������������ӽ��б�
# ��ӡ�б�
# n = 0
# lst =[]
# while n <3:
#     name = input('������������')
#     if name in lst:
#         print('�û�%s�Ѵ���'%name)
#     else:
#         lst.append(name)
#     n=n+1
# print(lst)

#��ϰ3 �û������û��������룬ֻҪ�û��������������l�е�ֵ����ʾ��½�ɹ���������ʾ��¼ʧ��
# l=[['alex','222'],['wusir','666'],['���ϰ�','123456']]
# name = input('����������')
# passwd = input('�������룺')
# for item in l:
#     if name==item[0] and passwd==item[1]:
#         print('��½�ɹ�')
#         break
# else:
#     print('��½ʧ��')

#�ж��ַ����ǲ�����ȫ���������
#s =' a '
#s1 =s.upper()
#s1=s.replace('a','v')
# s2 =s.strip()
# s2 =':'.join(['alex','3214','86'])
# print(s2)
#s1 = s.split(';')
#s2 = s.strip('<>')
#print(s2)
#print(s.isdigit())
#print(s.isalpha())

#Ԫ��
#days =('����һ','���ڶ�','������','������','������')
#�ֵ�
d= {
        'alex':'123',
        'david':'456'
    }
d['alex']=='123'