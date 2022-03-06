#定义关键字类  关键字驱动
import  requests
#解析多层嵌套的json数据格式
import jsonpath
import  json
class KeyDemo:

    #定义get请求方法：
    def get(self,url,headers=None,param=None):
        return requests.get(url=url,headers=headers,params=param)

    #定义post请求方法：
    def post(self,url,headers=None,data=None):
        if data is not None:
            data =self.json_dumps(data)
        return requests.post(url=url,headers=headers,data=data)
    #请求参数转化为json格式
    def json_dumps(self,data):
        return json.dumps(data)
    #校验字段获取方法
    def get_text(self,res,key):
        if res is not None:
            try:
                text = json.loads(res)         #将res数据转化成json格式
                value=jsonpath.jsonpath(text,'$..name'.format(key))   #从根路径开始找是否有name这个key，并获取value值
                #jsonpath 获取结果是list类型的值，如果获取失败则是false
                if value:
                    # 将list转化成String类型
                    if len(value)==1:
                        return value[0]
                    return value
            except Exception as e:
                return e
        else:
            return  None
