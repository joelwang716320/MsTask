__author__ = 'Administrator'

import json
import requests

# url
# payload = {'video_url': 'http://baidu.com', 'key2': ['value2', 'value3']}
loginUrl = 'https://login.api.guxiansheng.cn/index.php?c=user&a=login'
loginData = {'password':'123456','username':'17683240598','verify':'False'}

def loginApp():

    r = requests.post(url = loginUrl,data = loginData)

    loginReData = r.json()
#       print loginReData
#    udata = loginReData["data"]
#    member_id = udata["member_id"]
#    key = udata["key"]

    return r