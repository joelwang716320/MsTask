#coding=utf-8
__author__ = 'Administrator'
import requests
import random

from BaseData import inputData, utils
from BaseData import requestsData
from BaseData import loginResponseData


def askStock():
    """
    ask stock
    """

    inData = inputData
    key = loginResponseData.key
    member_id = loginResponseData.member_id
    STOCK_CODE = random.sample(inData.stock_code, 1)
    ASQuestions = inData.askStockQuestions
    askData = {'intro': ASQuestions,
               'key': key,
               'member_id': member_id,
               'stock_code': STOCK_CODE}
    askStockUrl = requestsData.askStockUrl

    rep = requests.post(url = askStockUrl, data = askData, verify = False)

    return rep

def testResult():
    requestCode = askStock().status_code
    messageCode = askStock().json()["code"]
    message = askStock().json()["message"]
    util = utils.myTools()
    if requestCode == 200 and messageCode == 1:
        util.add_row(["问股", "Successful", ""])
        return util
    else:
        util.add_row(["问股", "Failed", "requestCode = %s:massage = %s"%(requestCode,message)])
        return util
