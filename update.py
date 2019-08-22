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
  <title>Daily_update</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
  <script src="colors.js"> </script>
</head>
<body>
  <h1><a href="index.py"style="color:lightpink">Daily_Update</a></h1>
<div id="grid">
    <ol>
      {listStr}
    </ol>
    <div id="article">
    <h2>{title}</h2>
    {desc}
    <br><br><br>
    <a href="create.py">create</a>
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
  </div>
</div>

<input id="night_day" type="button" value="night" onclick="
  nightDayhandler(this);
">
</body>
</html>
'''.format(title=pageId,desc=description,listStr=view.getList(),form_default_title=pageId,form_default_description=description))
