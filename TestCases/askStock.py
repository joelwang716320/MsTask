#coding=utf-8
__author__ = 'Administrator'
import requests
from BaseData import utils
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

    return rep

def testResult():
    requestCode = askStock().status_code
    massageCode = askStock().json()
    massage = askStock().json()
    util = utils.myTools()
    if requestCode == 200 and massageCode == 1:
        util.add_row(["问股", "Successful", ""])
        return util
    else:
        util.add_row(["问股", "Failed", "requestCode = %s:massage = %s"%(requestCode,massage)])
