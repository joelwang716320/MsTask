__author__ = 'Administrator'
import json
import requests
from baseData import globalData

# url
askStockUrl = 'https://u.api.guxiansheng.cn/index.php?c=question&a=post'

def askStock():

    key = globalData.key
    member_id = globalData.member_id
    stock_code = 'sz000725'
    askData = {'intro':'testAskStock','key':key,'member_id':member_id,'stock_code':stock_code}
    rep = requests.post(url = askStockUrl,data = askData,verify = False)
    print rep.status_code
    print rep.json()

askStock()
