#coding=utf-8

__author__ = 'Administrator'

import requests

from BaseData import requestsData
from BaseData import inputData


def loginApp():

    loginUrl = requestsData.loginUrl
    loginData = inputData.loginData
    relogin = requests.post(url = loginUrl,data = loginData,verify = False)

    if relogin.status_code == 200 and relogin.json()["code"] == 1:
        print "登录成功..."
    else:
        print "请检查参数是否正确..."
    return relogin