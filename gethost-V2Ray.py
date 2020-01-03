#!/usr/bin/python
import base64
import time


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
        
        lineStr='{\n'
        lineStr=lineStr+'  "v": "2",\n'
        if (len(data)>1):
            lineStr=lineStr+'  "ps": "'+data[1]+'",\n'
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
#        print (lineStr64)
        t=t+1
finally:

    links_file = 'Url_Vmess_links_{}.txt'.format(time.strftime('%Y-%m-%d_%H-%M-%S'))
    f = open(links_file,'w',encoding='UTF-8', errors='ignore')
    f.write(lineStr64)
    f.close()
    file_object.close()
    
    ToBase64(links_file,'Base64_'+links_file)
    
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
    part = MIMEText("")
    msg.attach(part)
 
    #---附件部分---
    #链接文件附件
    part = MIMEApplication(open(links_file,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=links_file)
    msg.attach(part)
 
    #Base64编码后附件
    part = MIMEApplication(open('Base64_'+links_file,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename='Base64_'+links_file)
    msg.attach(part)
 
    send = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25
    send.login(_user, _pwd)#登陆服务器
    send.sendmail(_user, _to, msg.as_string())#发送邮件
    send.close()
