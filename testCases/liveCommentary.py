__author__ = 'Administrator'

import requests
from baseData import loginResponseData
from baseData import requestsData

def liveComment():
    """
    Live Room review
    """
    object_id = 7103
    tape = 3
    message = 'test for live comment'
    pid = 0
    appId = 'android'
    key = loginResponseData.key
    member_id = loginResponseData.member_id
    liveComData = {'object_id': object_id,
                   'type': tape,
                   'message': message,
                   'pid': pid,
                   'appId': appId,
                   'key': key,
                   'member_id': member_id,}
    liveComUrl = requestsData.liveCommentUrl
    reLiveCom = requests.post(url = liveComUrl,data = liveComData,verify = False)

    print "askStock :=====>%s"%reLiveCom.json()