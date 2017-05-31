__author__ = 'Administrator'

import json
import random
import requests
from baseData import loginResponseData
from baseData import requestsData

def putQuestion():
    """
    Ask the teacher questions about the Live Room
    """

    seller_id = 3333
    json_stock = ''
    questions = 'test for ask'
    answer_type = 2
    questions_way = 2
    appId = 'android'
    key = loginResponseData.key
    member_id = loginResponseData.member_id
    putData = {'seller_id': seller_id,
               'json_stock': json_stock,
               'questions': questions,
               'answer_type': answer_type,
               'questions_way': questions_way,
               'appId': appId,
               'key':key,
               'member_id':member_id}
    putQuestionUrl = requestsData.putQuestionUrl

    rePutQ = requests.post(url = putQuestionUrl,data = putData,verify = False)

    print "askStock :=====>%s"%rePutQ.json()


def getLiveStockInfo():

    seller_id = []
    liveStockUrl = requestsData.liveStockUrl
    re = requests.get(url = liveStockUrl,verify = False)

    reData =  re.json()
    listStock =  reData["data"]["list"]

    # get seller_id
    for i in  range(0,1):

        for i in range(0,len(listStock)-1):
            sellId = listStock[i]["seller_id"]
            seller_id.append(sellId)

        print seller_id
        randomSellerID = random.sample(seller_id,1)

        return randomSellerID


#    print listStock["seller_id"]
getLiveStockInfo()