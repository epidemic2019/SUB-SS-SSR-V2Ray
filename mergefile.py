#!/usr/bin/python3
import base64
import time
import sys,os
import socket

def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()


def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()

def merge(file1, file2,file3):
    f3 = open(file3, 'w', encoding='utf-8')
    with open(file1, 'r', encoding='utf-8') as f1:
#        f3.write('\n')
        for i in f1:
            f3.write(i)
    with open(file2, 'r', encoding='utf-8') as f2:
#        f3.write('\n')
        for i in f2:
            f3.write(i)

merge("url_ss_ssr.txt", "url_v2ray.txt","url_all.txt")
    
#生成指定文件名的base64文件
base64file_all="base64_all.txt"
links_file="url_all.txt"
ToBase64(links_file,base64file_all)

#发送邮件至指定邮箱
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
_user = "3158953@qq.com"
_pwd  = "ggohiqrvnrakbjgh"
_to   = "3158953@qq.com"

#如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = "服务器订阅文件-All"
msg["From"]    = _user
msg["To"]      = _to

#---文字部分---
part = MIMEText("订阅地址：\nhttps://zhuwei.netlify.com/base64_all.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_all.txt")
msg.attach(part)

#---附件部分---
#链接文件附件
part = MIMEApplication(open(links_file,'rb').read())
part.add_header('Content-Disposition', 'attachment', filename=links_file)
msg.attach(part)

#Base64编码后附件
part = MIMEApplication(open("base64_all.txt",'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="base64_all.txt")
msg.attach(part)

send = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25
send.login(_user, _pwd)#登陆服务器
send.sendmail(_user, _to, msg.as_string())#发送邮件
send.close()
