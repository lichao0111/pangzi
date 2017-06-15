#!/usr/bin/python
# edit richard
# 2017.6.13
# -*- coding: UTF-8 -*-
import os
import commands
import urllib
import urllib2
import json
#import requests


def scr_im():
    post_url = 'http://api.mozhan.com/ScreenShots/getUrls'
    req = urllib2.Request(post_url)
    response = urllib2.urlopen(req)
    url = json.load(response)
    str = url['d']
    for i in range(0, len(str)):
        name = str[i]['url']
        str1 = '/root/screenshot/phantomjs/bin/phantomjs /root/screenshot/resterize2.js ' + name
        open_files = commands.getstatusoutput(str1)
        mv_str = 'mv ' + name + '.png' + ' /root/screenshot/images/'
        open_files = commands.getstatusoutput(mv_str)
        id = str[i]['id']
        post_id(id)


def post_id(id):
    url1 = 'http://api.mozhan.com/ScreenShots/synResult'
    parmas = urllib.urlencode({'id': id})
    f = urllib.urlopen(url1, parmas)
    

def main():
    #scr_im()
    id = 10
    post_id(id)


if __name__ == "__main__":
    main()

