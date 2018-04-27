'''
通过对fanyi.youdao.com的html解析找到fanyi.min.js下的Response，再利用tool.oschina.net/codeformat/js进行格式化找到
salt的公式和sign的公式，如下：

salt = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)),

sign = n.md5("fanyideskweb" + t + i + "ebSeFb%=XZ%T[KZ)c(sy!")，其中t是要翻译的值，i是salt;

通过公式对salt和sign进行求解
'''
def getSalt():
    import time
    import random
    salt = int(time.time()*1000) + random.randint(0, 10)
    return salt

def md5(key):
    import hashlib
    md5 = hashlib.md5()

    # update需要bytes格式的参数
    md5.update(key.encode("utf-8"))

    value = md5.hexdigest()
    return value

def getSign(key, salt):
    sign = md5("fanyideskweb" + key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!")
    return sign

from urllib import request, parse

def youdao(key):

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    #为了保证salt的一致性，所以不能重复性调用
    salt = getSalt()

    data = {
        'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':str(salt),
        'sign':getSign(key, salt),
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'false'
    }

    #参数data需要bytes格式，因此需要parse
    data = parse.urlencode(data).encode()

    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        #不需要解压'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Content-Length':'200',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcUh0LIhDFy76NqDMemw; OUTFOX_SEARCH_USER_ID_NCOO=498899479.35822463; OUTFOX_SEARCH_USER_ID=-1744678099@61.183.146.148; SESSION_FROM_COOKIE=www.baidu.com; fanyi-ad-id=43155; fanyi-ad-closed=1; ___rl__test__cookies=1524790638341',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }



    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode()

    #通过eval将html转换成字典格式
    html = eval(html)
    #将翻译结果逐行显示
    #print(html)
    value1 = html['translateResult'][0][0]['tgt']
    print(key, ':', value1, sep='')
    value2 = html['smartResult']['entries']
    for item in value2:
        if item != '':
            print(key, ':', item, end='', sep='')

if __name__ == '__main__':
    key = input("请输入需要翻译的词：")
    youdao(key)
    while True:
        answer = input("是否需要继续翻译？（退出请输入q，继续翻译按任意键）")
        if answer == 'q':
            break
        else:
            key = input("请再次输入需要翻译的词：")
            youdao(key)


