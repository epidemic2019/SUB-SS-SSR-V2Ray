#!/usr/bin/python
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
msg["Subject"]="服务器订阅文件"
msg["From"]=_user
msg["To"]=_to
 
links_file=['url_ss_ssr.txt','url_v2ray.txt','url_all.txt','url_jj.txt','base64_ss_ssr.txt','base64_v2ray.txt','base64_all.txt','base64_jj.txt']
links_url=['https://zhuwei.netlify.com/base64_ss_ssr.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_ss_ssr.txt','https://zhuwei.netlify.com/base64_v2ray.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_v2ray.txt','https://zhuwei.netlify.com/base64_all.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_all.txt','https://zhuwei.netlify.com/base64_jj.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_jj.txt']


#---文字部分---
url=''
for value in links_url:
    url=url+value+"\n"
part=MIMEText('订阅地址：\n'+url)
msg.attach(part)
 
#---附件部分---
#链接文件附件
for value in links_file:
    part=MIMEApplication(open(value,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=value)
    msg.attach(part)
 
#Base64编码后附件
#part=MIMEApplication(open(base64file_v2ray,'rb').read())
#part.add_header('Content-Disposition', 'attachment', filename=base64file_v2ray)
#msg.attach(part)
 
send = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25
send.login(_user, _pwd)#登陆服务器
send.sendmail(_user, _to, msg.as_string())#发送邮件
send.close()
print('\n订阅文件发送邮箱完成！\n')