__author__ = 'Administrator'
import requests
from tests import requestsData
from tests import loginResponseData

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
    print rep.status_code
    print rep.json()

askStock()
