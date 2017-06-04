#coding=utf-8

from prettytable import PrettyTable
def myTools():
    x = PrettyTable(["测试点", "是否成功", "问题"])
    x.align["测试点"] = "l"  # Left align city names
    x.padding_width = 2  # One space between column edges and contents (default)

    return x

