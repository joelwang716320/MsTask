__author__ = 'Administrator'
from baseData import loginApp

# login app response info
loginReData = loginApp.loginApp().json()
udata = loginReData["data"]
member_id = udata["member_id"]
key = udata["key"]