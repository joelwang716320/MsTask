__author__ = 'Administrator'

import json
import random
import requests
from TestCases import askStock
from BaseData import inputData
from BaseData import loginResponseData
from BaseData import requestsData


SELLER_ID = []    # array of seller_id

def putQuestion():
    """
    Ask the teacher questions about the Live Room
    """

    getLiveStockInfo()  # init
    seller_id = random.sample(SELLER_ID,1)   # Remove an SELLER_ID from the array randomly
    putQ = inputData
    QUESTIONS = putQ.putQuestions
    json_stock = ''
    answer_type = 2
    questions_way = 2
    appId = 'android'
    key = loginResponseData.key
    member_id = loginResponseData.member_id
    putData = {'seller_id': seller_id,
               'json_stock': json_stock,
               'questions': QUESTIONS,
               'answer_type': answer_type,
               'questions_way': questions_way,
               'appId': appId,
               'key':key,
               'member_id':member_id}
    putQuestionUrl = requestsData.putQuestionUrl

    rePutQ = requests.post(url = putQuestionUrl,data = putData,verify = False)

    print "askStock :=====>%s"%rePutQ.json()

    return rePutQ


def getLiveStockInfo():

    global SELLER_ID
    liveStockUrl = requestsData.liveStockUrl
    re = requests.get(url = liveStockUrl,verify = False)

    reData =  re.json()
    listStock =  reData["data"]["list"]

    # Get an array of seller_id
    # seller_type=79    Filter out
    for i in  range(0,1):

        for i in range(0,len(listStock)-1):
            sellId = listStock[i]["seller_id"]
            SELLER_ID.append(sellId)

#    print listStock["seller_id"]
# getLiveStockInfo()
# print SELLER_ID
# print random.sample(SELLER_ID,1)

def putQResult():
    requestCode = putQuestion().status_code
    messageCode = putQuestion().json()["code"]
    message = putQuestion().json()["message"]
    util = askStock.testResult()
    if requestCode == 200 and messageCode == 1:
        util.add_row(["向老师提问", "Successful", ""])
        return util
    else:
        util.add_row(["向老师提问", "Failed", "requestCode = %s:massage = %s"%(requestCode,message)])