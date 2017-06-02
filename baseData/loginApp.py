__author__ = 'Administrator'

import requests

from baseData import requestsData
from baseData import inputData


def loginApp():

    loginUrl = requestsData.loginUrl
    loginData = inputData.loginData
    r = requests.post(url = loginUrl,data = loginData)

    return r