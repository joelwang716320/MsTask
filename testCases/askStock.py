__author__ = 'Administrator'
import requests
from baseData import requestsData
from baseData import loginResponseData

def askStock():
    """
    ask stock
    """

    key = loginResponseData.key
    member_id = loginResponseData.member_id
    stock_code = 'sz000725'
    askData = {'intro':'testAskStock',
               'key':key,
               'member_id':member_id,
               'stock_code':stock_code}
    askStockUrl = requestsData.askStockUrl

    rep = requests.post(url = askStockUrl,data = askData,verify = False)

    print "askStock :=====>%s"%rep.json()
