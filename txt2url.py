#!/usr/bin/python
import base64

f_url = open('Url_SS_SSR.txt','w',encoding='UTF-8', errors='ignore')
f_txt = open('host-SS.txt','r',encoding='UTF-8', errors='ignore')
try: 
    for line in f_txt:

        line=line.strip('\n')
        data=line.split('\t')
        server=data[1]
        server_port=data[2]
        password=data[3]
        password=str(base64.b64encode(password.encode("utf-8")), "utf-8")
        method=data[4]
        
        if (len(data)==7):
            protocol=data[5]
            obfs=data[6]
            group=str(base64.b64encode('免费-SSR服务器'.encode("utf-8")), "utf-8")
            lineStr=server+':'+server_port+':'+protocol+':'+method+':'+obfs+':'+password+'/?obfsparam=&group='+group
            lineStr='ssr://'+str(base64.b64encode(lineStr.encode("utf-8")), "utf-8")+'\n'
         
        else:
            protocol="origin"
            obfs="plain"
            group=str(base64.b64encode('免费-SS服务器'.encode("utf-8")), "utf-8")
            lineStr=method+':'+password+':'+server+':'+server_port
            lineStr='ss://'+str(base64.b64encode(lineStr.encode("utf-8")), "utf-8")+'\n'

        print (line)     
        f_url.write(lineStr)
finally:
    
    f_txt.close()
    f_url.close()