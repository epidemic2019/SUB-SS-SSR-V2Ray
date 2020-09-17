#!/usr/bin/python
import base64
t=0
t_ssr=0
count = len(open('host-SS.txt','r',encoding='UTF-8', errors='ignore').readlines())
# f = open('../gui-config.json','w')
f = open('../../ShadowsocksR-win-4.9.2/gui-config.json','w',encoding='UTF-8', errors='ignore')
file_object = open('host-SS.txt','r',encoding='UTF-8', errors='ignore')

lineStr='{\n'
# lineStr=lineStr+'  "version": "4.1.8.0",\n'
lineStr=lineStr+'  "configs": [\n'
f.write(lineStr)

try: 
    for line in file_object:

        numofproxy_ss = str(t+1).zfill(3)
        numofproxy_ssr = str(t_ssr+1).zfill(3)
        line=line.strip('\n')
        data=line.split('\t')
        server=data[1]
        server_port=data[2]
        password=data[3]
        method=data[4]
        
        if (len(data)==7):
            protocol=data[5]
        else:
            protocol="origin"
            
        if (len(data)==7):
            obfs=data[6]
        else:
             obfs="plain"
             
        lineStr='\t\t{\n'
#        lineStr=lineStr+'\t\t\t"remarks" : "",\n'
        lineStr=lineStr+'\t\t\t"server" : "'+server+'",\n'
        lineStr=lineStr+'\t\t\t"server_port" : '+server_port+',\n'
        lineStr=lineStr+'\t\t\t"server_udp_port" : 0,\n'
        lineStr=lineStr+'\t\t\t"password" : "'+password+'",\n'
        lineStr=lineStr+'\t\t\t"method" : "'+method+'",\n'
        if (len(data)==5):
            lineStr=lineStr+'\t\t\t"protocol" : "'+protocol+'",\n'
        else:
            lineStr=lineStr+'\t\t\t"protocol" : "origin",\n'        
        lineStr=lineStr+'\t\t\t"protocolparam" : "",\n'
        if (len(data)==7):
            lineStr=lineStr+'\t\t\t"obfs" : "'+obfs+'",\n'
        else:
            lineStr=lineStr+'\t\t\t"obfs" : "plain",\n'
        lineStr=lineStr+'\t\t\t"obfsparam" : "",\n'
        lineStr=lineStr+'\t\t\t"remarks_base64" : "",\n'

        if (len(data)==5):
            t=t+1
            lineStr=lineStr+'\t\t\t"group" : "放牧的风",\n'
            lineStr=lineStr+'\t\t\t"remarks" : "SS服务器-'+numofproxy_ss+'",\n'
            lineStr=lineStr+'\t\t\t"remarks_base64" : "'+str(base64.b64encode("SS服务器".encode("utf-8")), "utf-8")+'",\n'
        else:
            t_ssr=t_ssr+1
            lineStr=lineStr+'\t\t\t"group" : "放牧的风",\n'
            lineStr=lineStr+'\t\t\t"remarks" : "SSR服务器-'+numofproxy_ssr+'",\n'
            lineStr=lineStr+'\t\t\t"remarks_base64" : "'+str(base64.b64encode("SSR服务器".encode("utf-8")), "utf-8")+'",\n'
         
        lineStr=lineStr+'\t\t\t"enable" : true,\n'
        lineStr=lineStr+'\t\t\t"udp_over_tcp" : false\n'
        
        t=t+1
        t_ssr=t_ssr+1
        if t==count:
            lineStr=lineStr+'    }\n'
        else:
            lineStr=lineStr+'    },\n'
#        print (lineStr)
        f.write(lineStr)
finally:

    f2 = open('tail-SS.txt','r',encoding='UTF-8', errors='ignore')
    
    lines = f2.readlines()
    for line3 in lines:
        f.write(line3)
    file_object.close()
    f.close()
    f2.close()