#!/usr/bin/env/python
# -*-coding:utf-8-*-
import pytest
import requests


@pytest.fixture()
def must_run():
    print "must run function"


# @pytest.fixture(params=[{"url": "http://emp.boryiot.com/admin/login.aspx",
#                          "username": "admin",
#                          "password": "admin888"}])
# def login(request):
#     print "login"
#     url = request.param["url"]
#     username = request.param["username"]
#     password = request.param["password"]
#     response = requests.post(url, json={"txtUserName": username, "txtPassword": password})
#     print "status_code:", response.status_code
#     print "code", response.text
#     return response.cookies

@pytest.fixture(params=[{"url": "http://eolinker.chatm.com/eolinker/server/index.php?g=Web&c=Guest&o=login",
                         "info": {
                             "loginName": "peixiaomin",
                             "loginPassword": "4e44d3bdb9a1ac4a19861580bc042ce4"
                              },
                         "header": {'content-type': "application/x-www-form-urlencoded;charset=UTF-8"}
                         }]
                )
def login(request):
    print "login"
    url = request.param["url"]
    response = requests.post(url, data=request.param["info"], headers=request.param["header"])
    print "status_code:", response.status_code
    print "code", response.ok
    cookies = response.cookies.get_dict()
    return cookies
