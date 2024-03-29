#!C:\Program Files (x86)\Python\Python37-32\python.exe
print("Content-Type: text/html");
print()
import cgi, os,view


form=cgi.FieldStorage()
if 'id' in form:
    pageId=form["id"].value
    description = open('data/'+pageId,'r').read()
    description=description.replace('<','&lt;')
    description=description.replace('>','&gt;')
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action='''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId='Welcome'
    description = 'Share and update your study.'
    update_link = ''
    delete_action=''
print('''<!doctype html>
<html>
<head>
  <title>Daily_Study</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
  <script src="colors.js"> </script>
</head>
<body>
  <h1><a href="index.py"style="color:lightpink">Daily_Study</a></h1>
<div id="grid">
    <ol>
      {listStr}
    </ol>
    <div id="article">
    <h2>{title}</h2>
    {desc}<br><br>
        <a href="create.py">create</a>
        {update_link}
        {delete_action}
    </form>
  </div>
</div>

<input id="night_day" type="button" value="night" onclick="
  nightDayhandler(this);
">
</body>
</html>
'''.format(title=pageId,desc=description,listStr=view.getList(),update_link=update_link,delete_action=delete_action))
