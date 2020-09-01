import requests
import hashlib
import re

req = requests.session()
url = "http://docker.hackthebox.eu:31778"

#GET request
rget = req.get(url)
html = rget.content.decode('utf-8')

#Strip HTML
def html_tags(html):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)

#Split return string
a = html_tags(html)
b = a.split('string')[1]
c = b.rstrip()

#MD5 encryption / Before encryption encode string
enhash1 = c.encode('utf-8')
enhash2 = hashlib.md5(enhash1).hexdigest()

#Post request
data = dict(hash=enhash2)
rpost = req.post(url=url, data=data)

#Print answer
print(rpost.text)
