__author__ = 'Administrator'

from tests import loginApp

# login app response info
loginReData = loginApp.loginApp().json()
udata = loginReData["data"]
member_id = udata["member_id"]
key = udata["key"]