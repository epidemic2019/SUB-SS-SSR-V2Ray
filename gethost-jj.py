#!/usr/bin/python
import requests
url = 'https://jj-rss-01.best/link/CR0fY9iH5GntsUxi?sub=1'
r = requests.get(url, allow_redirects=True)  # to get content after redirection
pdf_url = r.url # 'https://media.readthedocs.org/pdf/django/latest/django.pdf'
with open('base64_jj.txt', 'wb') as f:
    f.write(r.content)