import logging
import time
from logging import handlers
#logging分为五个等级，默认只显示warning等级以上的信息
logging.debug('debug message')   #情况最轻
logging.info('info message')     #信息类日志
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')


sh = logging.StreamHandler()  #写到屏幕上
fh = logging.FileHandler(filename='xxx.log',encoding='utf-8')   #写到文件上
fh1 =logging.handlers.RotatingFileHandler('myapp1.log',maxBytes=512,backupCount=5,encoding='utf-8')    #RotatingFileHandler 根据大小切割文件
fh2 =logging.handlers.TimedRotatingFileHandler(filename='myapp2.log',when='H',interval=5,encoding='utf-8')  #TimedRotatingFileHandler根据时间切割
                                                #when 根据 秒s 小时H 天D  周W
logging.basicConfig(level=logging.WARNING,   #默认显示level等级以上的信息
                    handlers=[sh,fh,fh1,fh2],
                    datefmt='%Y-%m-%d %H:%M:%S',
                    #指定日志格式
                    format='%(asctime)s - %(name)s[%(lineno)d] -%(levelname)s -%(module)s: %(message)s')
                    #[%(lineno)d] ：记录第几行
while True:
    logging.warning('警告信息：程序异常')
    time.sleep(0.3)
