#!/usr/bin/python
import requests
import base64
import chardet

#url = 'https://jj-rss-01.best/link/CR0fY9iH5GntsUxi?sub=1'
url = 'https://jj-rss-01.best/link_diy/PeHDxttH7wt3vDKe?t=1'



r = requests.get(url, allow_redirects=True)  # to get content after redirection
print(chardet.detect(r.content))
#if chardet.detect(base64.b64decode(r.content))['encoding']=='ascii':
if chardet.detect(r.content)['encoding']=='ascii':
    str_line=base64.b64decode(r.content).decode().split('\n')
    keys=['ss://','ssr://','vess://']
    for value in keys:
        if str_line[0].find(value)>=0:
           with open('base64_jj.txt', 'wb') as f:
               f.write(r.content)
               f.close
           print('\n几鸡订阅更新完成！')
else:
    print('\n几鸡订阅地址不可用或尝试关闭代理后更新！')