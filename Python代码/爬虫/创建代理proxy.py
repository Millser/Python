from urllib import request
#爬虫的网址
url = "http://www.baidu.com"

#创建代理
proxy = {'http':'123.207.245.211'}
#创建handlers
handlers = request.ProxyHandler(proxy)
#创建opener
opener = request.build_opener(handlers)
#安装opener
request.install_opener(opener)


respose = request.urlopen(url)

html = respose.read().decode()

print(html)

