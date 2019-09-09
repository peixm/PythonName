#!/usr/bin/env/python
# -*-coding:utf-8-*-


def verifyStatusCode(response):
    info = {"status": True,
            "info": "success"}
    if response.status_code != 200:
        info["status"] = False
        info["info"] = "The status_code is error"
        return info
    if response.json()["statusCode"] != "000000":
        info["status"] = False
        info["info"] = "The statusCode is error"
        return info
    return info

