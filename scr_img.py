#!/usr/bin/python
# edit richard
# 2017.6.13
# -*- coding: UTF-8 -*-
from email.mime.text import MIMEText
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
from email.header import Header
import requests
import re, os, time
import smtplib
import commands
import urllib
import urllib2
import json
import qiniu.config


def up_imges(name):
    access_key = 'xxxxxxxxxxxxxxxxxxxxxx'
    secret_key = 'xxxxxxxxxxxxxxxxxxxxxx'
    q = Auth(access_key, secret_key)
    bucket_name = 'mz-style'
    key = name
    token = q.upload_token(bucket_name, key, 3600)
    localfile = '/data1/screenshot/'+name
    try:
        ret, info = put_file(token, key, localfile)
        src_log("%s up qiniu ok \n" %name) 
    except:
        src_log("%s up qiniu error" %name)


def send_mail(str):
    mail_host = "smtp.qq.com"
    mail_user = "649807430@qq.com"
    mail_pass = "xxxxxxx"

    sender = '649807430@qq.com'
    receivers = 'lichao0111@163.com;649807430@qq.com'

    message = MIMEText(str, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = receivers
    subject = 'screen image service'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, "465")
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print "ok"
    except smtplib.SMTPException, e:
        print e


def scr_im():
    post_url = 'http://api.mozhan.com/ScreenShots/getUrls'
    try:
        req = urllib2.Request(post_url)
        response = urllib2.urlopen(req)
        url = json.load(response)
    except:
        error_str = 'conn getUrls error'
        src_log(error_str)
        send_mail(error_str)
    # else:
    #     log() 'getUrls ok!'
    str = url['d']
    for i in range(0, len(str)):
        name = str[i]['url']
        str1 = '/data1/screenshot/phantomjs/bin/phantomjs /data1/screenshot/resterize2.js ' + name
        open_files = commands.getstatusoutput(str1)
        image_name=name+'.png'
        log = '%s screen_image is ok' % name
        src_log(log) 
        up_imges(image_name)
        mv_str = 'mv ' + name + '.png' + ' /data1/screenshot/images/'
        open_files = commands.getstatusoutput(mv_str)
        id = str[i]['id']
        post_id(id)


def post_id(id):
    try:
        url1 = 'http://api.mozhan.com/ScreenShots/synResult'
        parmas = urllib.urlencode({'id': id})
        f = urllib.urlopen(url1, parmas)
    # print f
    except:
        error_log = 'conn synResult error'
        src_log(error_log)
        send_mail(error_log)
    else:
        print '%s anything ok' %id


def src_log(log):
    try:
        fh = open("scr_img.log", "a")
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        start_log = "date: %s-----------------------" % date_time
        fh.write(start_log)
        fh.write(log)
    except IOError:
        print "Error log"
        fh.write("-------------------------")
    else:
        fh.write("\n")
        fh.write("-------------------------")
        fh.close()


def main():
#    while 0:
     scr_im()
#       time.sleep(3600)


if __name__ == "__main__":
    main()
