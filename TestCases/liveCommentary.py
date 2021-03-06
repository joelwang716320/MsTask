#coding=utf-8

__author__ = 'Administrator'

import random
import requests
from BaseData import inputData
from BaseData import loginResponseData
from BaseData import requestsData
from TestCases import putQuestions

SELLERID = []
OBJECT_ID = []
KEY = loginResponseData.key
MEMBER_ID = loginResponseData.member_id
def liveComment():
    """
    Live Room review
    """

    liveMessage = inputData
    MESSAGE = random.sample(liveMessage.commentContent, 3)
    util = putQuestions.putQResult()
    for i in range(0,3):
        getLiveComment() # init
        liveComData = {'object_id': OBJECT_ID,
                       'type': 3,
                       'message': MESSAGE[i],
                       'pid': 0,
                       'appId': 'android',
                       'key': KEY,
                       'member_id': MEMBER_ID}
        liveComUrl = requestsData.liveCommentUrl
        reLiveCom = requests.post(url = liveComUrl,data = liveComData,verify = False)

        requestCode = reLiveCom.status_code
        messageCode = reLiveCom.json()["code"]
        message = reLiveCom.json()["message"]
        if requestCode == 200 and messageCode == 1:
            util.add_row(["直播间评论_%s"%i, "Successful", ""])
#            return util
        else:
            util.add_row(["直播间评论_%s"%i, "Failed", "requestCode = %s:massage = %s" % (requestCode, message)])
#            return util

        print "askStock :=====>%s"%reLiveCom.json()
        print OBJECT_ID
    print util



def getLiveComment():
    """
    First, get to the teacher ID and then get the teacher's dynamic(PolicyID)
    """
    global SELLERID
    global OBJECT_ID
    putQuestions.getLiveStockInfo()
    SELLERID = random.sample(putQuestions.SELLER_ID,1)

    policyData = {'seller_id': SELLERID,
                  'is_history_point': 0,
                  'refresh': 0,
                  'pagesize': 1,  # Show the latest one
                  'appId': 'android',
                  'key': KEY,
                  'member_id': MEMBER_ID}

    liveCimmentArrayUrl = requestsData.liveCimmentArrayUrl
    getResponData = requests.get(url = liveCimmentArrayUrl,params = policyData,verify = False)
    reData = getResponData.json()

    policyID = reData['data']['policy_list'][0]['policy_id']
    OBJECT_ID = policyID