#!#flask/bin/python
#coding:utf-8
from app import app
from flask import Flask, request, redirect, url_for, render_template, abort, session, escape, send_from_directory, flash,g,make_response
# from app import db,models,aes,utils
import datetime,time
import os

# from config import BASE_INFO_FILE
# from config import REDIRECT_FILE
# from config import BASE_DIR
# from config import CURRENT_INFO

# from config import country_list2 
# from config import COUNTRY_LIST
import pickle
import json
import hashlib

import requests

@app.route('/')
def first():
    return "Hello World!"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/test",methods=["GET","POST"])
def base():
    if request.method == "GET":
        release = request.args.get("release","0")
        print release
        return str(request.args)
    else :
        state = request.form.get("state","1")
        return "post" 

@app.route("/weixin",methods=["POST"])
def weixin_post():
    return "post"

@app.route("/weixin",methods=["GET"])
def weixin():
    try:
        data = request.args
        if len(data) == 0:
            return "hello, this is handle view"
        signature = data.get("signature","0")
        timestamp = data.get("timestamp","0")
        nonce = data.get("nonce","0")
        echostr = data.get("echostr","0")
        token = "weixin" #请按照公众平台官网\基本配置中信息填写

        print str(data)
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return echostr
        else:
            return "ok"
    except:

        return "fail"


# def handle():
#     try:
#             webData = web.data()
#             print "Handle Post webdata is ", webData   #后台打日志
#             recMsg = receive.parse_xml(webData)
#             if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
#                 toUser = recMsg.FromUserName
#                 fromUser = recMsg.ToUserName
#                 content = "test"
#                 replyMsg = reply.TextMsg(toUser, fromUser, content)
#                 return replyMsg.send()
#             else:
#                 print "暂且不处理"
#                 return "success"
#         except Exception, Argment:
#             return Argment

	# try:
 #        # data = web.input()
 #        data = ["ss","ddd"]
 #        # data = request.args
 #        if len(data) == 0:
 #            return "hello, this is handle view"
 #        signature = data.get("signature","0")
 #        timestamp = data.get("timestamp","0")

 #        nonce = data.get("nonce","0")
 #        echostr = data.get("echostr","0")
 #        token = "weixin" #请按照公众平台官网\基本配置中信息填写

 #        list = [token, timestamp, nonce]
 #        list.sort()
 #        sha1 = hashlib.sha1()
 #        map(sha1.update, list)
 #        hashcode = sha1.hexdigest()
 #        print "handle/GET func: hashcode, signature: ", hashcode, signature
 #        if hashcode == signature:
 #            return echostr
 #        else:
 #            return ""
 #    except Exception, Argument:
 #        return Argument
