# __author__="richard"
# coding=utf-8
#用requests 写的获取天气，使用QQ邮箱进行发邮件
#注意点：qq邮箱使用授权码，授权码在QQ邮箱设置中获取，需要使用SMTP_SSL加密发送，message中的to 和from 要是收件人和发件人，多收件人可以使用分号隔开
#2016年12月12日 10:43:51

from email.mime.text import MIMEText
from email.header import Header
import requests
import re,json
import smtplib

URL = 'http://api.jirengu.com/weather.php?'

def open_url(url):
    heads = {"Accept": "text/html,application/xhtml+xml,application/xml;",
             "Accept-Encoding": "gzip",
             "Accept-Language": "zh-CN,zh;q=0.8",
             "Referer": "http://www.douyu.com/",
             "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
             }
    r = requests.get(url,heads)
    r.encoding='utf-8'
    if r.status_code != 200:
        print "nothing"
    else:
        return r.text

def sendmail_test():

    wt = json.loads(open_url(URL))
    date = wt["date"]
    city = wt["results"][0]["currentCity"]
    pm = wt["results"][0]["pm25"]
    weather = wt["results"][0]["weather_data"][0]["weather"]
    temperature = wt["results"][0]["weather_data"][0]["temperature"]
    str = "city: %s day:%s pm2.5:%s weather:%s temperature:%s " %(city,date,pm,weather,temperature)

    mail_host = "smtp.qq.com"
    mail_user = "649807430@qq.com"
    mail_pass = "*******"  #授权码

    sender = '649807430@qq.com'
    receivers ='lichao0111@163.com;649807430@qq.com'

    message = MIMEText(str, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = receivers
    subject = '厦门天气预报 '
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,"465")
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print "ok"
    except smtplib.SMTPException, e:
        print e

if __name__=="__main__":
    sendmail_test()