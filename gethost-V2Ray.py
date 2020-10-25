#!/usr/bin/python
import base64
import time
import sys,os
import socket
from qqwry import QQwry
q = QQwry()
q.load_file('qqwry.dat')

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

#ToBase64("./desk.jpg",'desk_base64.txt')  # 文件转换为base64
#ToFile("./desk_base64.txt",'desk_cp_by_base64.jpg')  # base64编码转换为二进制文件



t=0
count = len(open('host-V2Ray.txt','r',encoding='UTF-8', errors='ignore').readlines())
# f = open('../gui-config.json','w')
#f = open('Url_Vmess.txt','w',encoding='UTF-8', errors='ignore')
file_object = open('host-V2Ray.txt','r',encoding='UTF-8', errors='ignore')

lineStr64=''
try: 
    for line in file_object:
        line=line.strip('\n')
        data=line.split('\t')
        
        numofproxy = str(t+1).zfill(3)

        server_name = socket.getaddrinfo(data[1], None)
        server_ip=server_name[0][4][0]
 
        location=q.lookup(server_ip)
        country=location[0]    
       
        lineStr='{\n'
        lineStr=lineStr+'  "v": "2",\n'
        if (len(data)>1):
            lineStr=lineStr+'  "ps": "'+country+'-V2Ray-'+numofproxy+'",\n'
        else:
            lineStr=lineStr+'  "ps": "",\n'
        if (len(data)>1):
            lineStr=lineStr+'  "add": "'+data[1]+'",\n'
        else:
            lineStr=lineStr+'  "add": "",\n'
        if (len(data)>2):
            lineStr=lineStr+'  "port": "'+data[2]+'",\n'
        else:
            lineStr=lineStr+'  "port": "",\n'
        if (len(data)>3):
            lineStr=lineStr+'  "id": "'+data[3]+'",\n'
        else:
            lineStr=lineStr+'  "id": "",\n'
        lineStr=lineStr+'  "aid": "0",\n'
        if (len(data)>4):
            lineStr=lineStr+'  "net": "'+data[4]+'",\n'
        else:
            lineStr=lineStr+'  "net": "",\n'
        lineStr=lineStr+'  "type": "none",\n'
        lineStr=lineStr+'  "host": "",\n'
        if (len(data)>5):
            lineStr=lineStr+'  "path": "'+data[5]+'",\n'
        else:
            lineStr=lineStr+'  "path": "",\n'
        if (len(data)>6):
            lineStr=lineStr+'  "tls": "'+data[6]+'"\n'
        else:
            lineStr=lineStr+'  "tls": ""\n'
        lineStr=lineStr+'}\n'
        
        lineStr64=lineStr64+'vmess://'+str(base64.b64encode(lineStr.encode("utf-8")), "utf-8")+'\n'
#        print (lineStr)
        t=t+1
finally:

    #添加自建服务器vmess链接至订阅文件
    file_ownerurl = open('owner_url_v2ray.txt','r',encoding='UTF-8', errors='ignore')
    line_ownerurl = ''
    for line in file_ownerurl:
        line_ownerurl = line_ownerurl+line        
    lineStr64 = lineStr64+line_ownerurl
    #End

    #links_file = 'Url_Vmess_links_{}.txt'.format(time.strftime('%Y-%m-%d_%H-%M-%S'))
    links_file='url_v2ray.txt'
    
    if os.path.exists(links_file):
        if os.path.exists(links_file+'.bak'):
            os.remove(links_file+'.bak')
        os.rename(links_file,links_file+'.bak')
    f = open(links_file,'w',encoding='UTF-8', errors='ignore')
    f.write(lineStr64)
    f.close()
    file_object.close()
    file_ownerurl.close()
    
    #生成指定文件名的base64文件
    base64file_v2ray='base64_v2ray.txt'
    ToBase64(links_file,base64file_v2ray)
    
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
    msg["Subject"] = "服务器订阅文件-V2Ray"
    msg["From"]    = _user
    msg["To"]      = _to
 
    #---文字部分---
    part = MIMEText("订阅地址：\nhttps://zhuwei.netlify.com/base64_v2ray.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_v2ray.txt")
    msg.attach(part)
 
    #---附件部分---
    #链接文件附件
    part = MIMEApplication(open(links_file,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=links_file)
    msg.attach(part)
 
    #Base64编码后附件
    part = MIMEApplication(open(base64file_v2ray,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=base64file_v2ray)
    msg.attach(part)
 
    send = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25
    send.login(_user, _pwd)#登陆服务器
    send.sendmail(_user, _to, msg.as_string())#发送邮件
    send.close()
