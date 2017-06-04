#coding=utf-8

import requests
from TestCases import askStock
from BaseData import loginResponseData, requestsData

KEY = loginResponseData.key
MEMBERID = loginResponseData.member_id

util = askStock.testResult()
def sign():
    data = {'key': KEY,
            'member_id': MEMBERID}
    reSign = requests.post(url = requestsData.signUrl, data = data, verify = False)

    if reSign.json()["code"] == 1 and reSign.status_code == 200:
        util.add_row(["签到", "Successful", ""])
    elif reSign.json()["code"] == 3 and reSign.status_code == 200:
        util.add_row(["签到", "已签到", "您已经签到啦"])
    else:
        util.add_row(["签到", "Failed", "requestCode = %s:massage = %s"%(reSign.status_code,reSign.json()["message"])])

    return util