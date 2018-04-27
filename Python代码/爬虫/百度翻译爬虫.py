#利用parse模块模拟post请求

from urllib import request, parse
import json

#开始的url
baseurl = 'http://fanyi.baidu.com/sug'

q = 1
#进入循环，并提示用户输入翻译的词
while q != 'q':
    #用户输入需要翻译的词
    word = input("请输入需要翻译的单词：")

    # 构建数据的字典
    data = {}

    #将用户输入的词加入到字典中
    data['kw'] = word

    #需要用parse对data进行编码
    data = parse.urlencode(data).encode("utf-8")

    #构建一个Request的请求
    respose = request.Request(url=baseurl, data=data)

    respose = request.urlopen(respose)

    json_data = respose.read().decode("utf-8")

    #将json字符串转换成字典，用for循环将字典里的词读取出来
    json_data = json.loads(json_data)

    for item in json_data['data']:
        print(item['k'],':',item['v'])

    q = input("是否想要继续翻译（输入q退出）：")

