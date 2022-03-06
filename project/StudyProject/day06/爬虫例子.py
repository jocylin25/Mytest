__author__ = 'admin'
#爬取豆瓣电影第一页例子
import re
from urllib.request import urlopen
ret= urlopen('https://movie.douban.com/top250?start=0&filter')
html_content =ret.read().decode('utf-8')
pattern='<div class="item">.*?<div class="pic">.*?<em class="">(P<id>\d+).*?</em></div><span class="title">(?P<movie_name>.*?)</span>'
ret1 =re.finditer(pattern,html_content,flags=re.S)
for i in ret1:
    print(i.group('id'),i.group('movie_name'))