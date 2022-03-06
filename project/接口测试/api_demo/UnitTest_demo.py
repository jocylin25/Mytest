import unittest
from api_keyword.keyword_demo import KeyDemo
#引入config
import configparser
#引入数据驱动
from ddt import ddt,file_data
#创建一个UnitTest测试用例管理框架
@ddt       #应用装饰器
class ApiCases(unittest.TestCase):
   #setUpClass（）类提取公共部分，每次框架运行只执行一次 ，作为初始化用例中要用到的数据和对象  setUp（）每个case运行前都执行一次
    @classmethod       #装饰器声明
    def setUpClass(cls) ->None:
        cls.token=None
        #实例化需要的内容
        conf =configparser.ConfigParser()
        #测试数据
        conf.read('../config/config.ini')
        cls.kd =KeyDemo()
        cls.url =conf.get('DEFAULT','url')

    #测试用例1
    @file_data('../data/login.yaml')
    def test_1_api_demo(self,**kwargs):
        #获取config中url
        url =self.url+ kwargs['path']
        #执行测试
        res =self.post(url=url,data=kwargs['data'])
        print(res.text)
        #获得实际结果
        value =self.get_text(res.text,'name')
        #断言
        self.assertEqual(first=kwargs['ex_result'],second=value,msg='获取信息失败')  #first预期值 在yaml文件内 second实际值

    #测试用例2
    @file_data('../data/enter.yaml')
    def test_2_api_demo(self,**kwargs):

        #获取config中url
        url =self.url+ kwargs['path']
        #执行测试,访问登陆接口
        res =self.kd.post(url=url,headers=['headers'],data=kwargs['data'])

        #提取msg内容，作为断言使用
        value =self.kd.get_text(res.text,'msg')
        #获取token
        ApiCases.token =self.kd.get_text(res.text,'token')    #ApiCases.token 给cls.token赋值 将token保存在全局变量
        #断言校验
        self.assertEqual(first=kwargs['ex_result'],second=value,msg='获取信息失败')  #first预期值 在yaml文件内 second实际值

    def test_3_token(self):
        #将之前赋值的token进行调用
        print(self.token)


if __name__ =='__main__':
    unittest.main()





