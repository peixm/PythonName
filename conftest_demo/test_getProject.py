#!/usr/bin/env/python
# -*-coding:utf-8-*-
import requests


def test_update(login):

    url = "http://eolinker.chatm.com/eolinker/server/index.php?g=Web&c=Project&o=getProject"
    param = {
        "projectID": "42",
            }

    header = {"content-type": "application/x-www-form-urlencoded;charset=UTF-8"}

    #客户端发送请求道服务器
    r = requests.post(url, data=param, headers=header, cookies=login)
    responsedata = r.json()

    print '服务端的响应数据：', responsedata
    print "get the status:", r.status_code

    assert r.status_code == 200, "status_code is {0}".format(r.status_code)
    assert r.json()["statusCode"] == "000000", "statusCode is {0}".format(r.json()["statusCode"])