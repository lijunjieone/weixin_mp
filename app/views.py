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

import requests

@app.route('/')
def first():
    return "Hello World!"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/weixin")
def weixin():
	try:
        data = web.input()
        if len(data) == 0:
            return "hello, this is handle view"
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "xxxx" #请按照公众平台官网\基本配置中信息填写

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception, Argument:
        return Argument
