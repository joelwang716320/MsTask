__author__ = 'Administrator'
import requests
from BaseData import inputData
from BaseData import requestsData
from BaseData import loginResponseData

def askStock():
    """
    ask stock
    """

    inData = inputData
    key = loginResponseData.key
    member_id = loginResponseData.member_id
    STOCK_CODE = inData.stock_code
    ASQuestions = inData.askStockQuestions
    askData = {'intro':ASQuestions,
               'key':key,
               'member_id':member_id,
               'stock_code':STOCK_CODE}
    askStockUrl = requestsData.askStockUrl

    rep = requests.post(url = askStockUrl,data = askData,verify = False)

    print "askStock :=====>%s"%rep.json()
