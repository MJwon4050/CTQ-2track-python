#!python
#전 과제를 한글로 입력하고 utf-8을 적용시키는 법을 모르는 바람에 싹 다 지우고 어쩔 수 없이 영상과 동일하게 작성했습니다..이거 때문에 3시간동안 고생했네...
print("Content-Type: text/html")
print()
import cgi,os,view
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hi Jaewon'
    update_link = ''
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">creat</a>
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId,
    desc=description,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action))
