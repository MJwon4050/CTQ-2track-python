#!python
#전 과제를 한글로 입력하고 utf-8을 적용시키는 법을 모르는 바람에 싹 다 지우고 어쩔 수 없이 영상과 동일하게 작성했습니다..이거 때문에 3시간동안 고생했네...
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hi Jaewon'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=CTQ">CTQ</a></li>
    <li><a href="index.py?id=JAEWONMIN">JAEWONMIN</a></li>
    <li><a href="index.py?id=Seil">Seil</a></li>
    <li><a href="index.py?id=nothing">nothing</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description))
