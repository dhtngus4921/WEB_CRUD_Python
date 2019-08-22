#!C:\Program Files (x86)\Python\Python37-32\python.exe
print("Content-Type: text/html");
print()
import cgi, os,view

form=cgi.FieldStorage()

if 'id' in form:
    pageId=form["id"].value
    description = open('data/'+pageId,'r').read()
else:
    pageId='Welcome'
    description = 'Share and update your study.'


print('''<!doctype html>
<html>
<head>
  <title>Daily_create</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
  <script src="colors.js"> </script>
</head>
<body>
  <h1><a href="index.py"style="color:lightpink">Daily_Create</a></h1>
<div id="grid">
    <ol>
      {listStr}
    </ol>
    <div id="article">
    <h2>{title}</h2>
    {desc}<br><br>

    <form action="process_create.py" method="post">
        <a href="create.py">create</a>
        <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
  </div>
</div>

<input id="night_day" type="button" value="night" onclick="
  nightDayhandler(this);
">
</body>
</html>
'''.format(title=pageId,desc=description,listStr=view.getList()))
