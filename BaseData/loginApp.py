__author__ = 'Administrator'

import requests

from BaseData import requestsData
from BaseData import inputData


def loginApp():

    loginUrl = requestsData.loginUrl
    loginData = inputData.loginData
    r = requests.post(url = loginUrl,data = loginData)

    return r