__author__ = 'Administrator'

import requests
from baseData import globalData

seller_id = 707
json_stock=''
questions = 'test for ask'
answer_type = 2
questions_way = 2
appId = 'android'
def putQuestion():
    putData = {'seller_id': seller_id,
               'json_stock':'',
               'questions': questions,
               'answer_type': answer_type,
               'questions_way': questions_way,
               'appId': appId}
    putQuestionUrl = globalData.putQuestionUrl
    rePutQ = requests.post(url = putQuestionUrl,data = putData)

