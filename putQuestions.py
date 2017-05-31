__author__ = 'Administrator'

import requests
from tests import loginResponseData
from tests import requestsData

def putQuestion():
    """
    Ask the teacher questions about the Live Room
    """

    seller_id = 676
    json_stock=''
    questions = 'test for ask'
    answer_type = 2
    questions_way = 2
    appId = 'android'
    key = loginResponseData.key
    member_id = loginResponseData.member_id
    putData = {'seller_id': seller_id,
               'json_stock':'',
               'questions': questions,
               'answer_type': answer_type,
               'questions_way': questions_way,
               'appId': appId,
               'key':key,
               'member_id':member_id}
    putQuestionUrl = requestsData.putQuestionUrl

    rePutQ = requests.post(url = putQuestionUrl,data = putData,verify = False)

    print rePutQ.status_code
    print rePutQ.json()

putQuestion()