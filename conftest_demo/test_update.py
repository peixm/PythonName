#!/usr/bin/env/python
# -*-coding:utf-8-*-
import requests
from conftest_demo.tool import responseHelper

def test_update(login):

    url = "http://eolinker.chatm.com/eolinker/server/index.php?g=Web&c=Project&o=editProject"
    param = {
        "projectID": "42",
        "projectName": "test111",
        "projectVersion": 1.0,
        "projectType": 0,
        "isAdd": False
            }

    header = {"content-type": "application/x-www-form-urlencoded;charset=UTF-8"}

    #客户端发送请求道服务器
    r = requests.post(url, data=param, headers=header, cookies=login)
    # r = requests.post(url, data=param, headers=header)

    responsedata = r.json()

    print '服务端的响应数据：', responsedata
    print "get the status:", r.status_code
    print "info:", responseHelper.verifyStatusCode(r)
    assert True == responseHelper.verifyStatusCode(r).get('status'), responseHelper.verifyStatusCode(r).get('info')
    # assert r.status_code == 200, "status_code is {0}".format(r.status_code)
    # assert r.json()["statusCode"] == "000000", "statusCode is {0}".format(r.json()["statusCode"])