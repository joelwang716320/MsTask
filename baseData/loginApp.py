__author__ = 'Administrator'

import requests

from baseData import requestsData


def loginApp():

    loginUrl = requestsData.loginUrl
    loginData = requestsData.loginData
    r = requests.post(url = loginUrl,data = loginData)

    return r