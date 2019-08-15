#!C:\Program Files (x86)\Python\Python37-32\python.exe
print("Content-Type: text/html");
print()
import cgi, os

files = os.listdir('data')
listStr= ''
for item in files:
    listStr = listStr+'<li><a href="index.py?id={name}"</a></li>'.format(name=item)

form=cgi.FieldStorage()
if 'id' in form:
    pageId=form["id"].value
    description = open('data/'+pageId,'r').read()
else:
    pageId='Welcome'
    description = 'Hello, Travel'

print('''<!doctype html>
<html>
<head>
  <title>TRAVEL1-Explanation</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
  <script src="colors.js"> </script>
</head>
<body>
  <h1><a href="index.py"style="color:lightpink">TRAVEL</a></h1>
<div id="grid">
    <ol>
      {listStr}
    </ol>
  <div id="article">
    <h2>{title}</h2>
    {desc}
    <p>
        <img src="{title}.jpg" width="50%">
    </p>
  </div>
</div>

<input id="night_day" type="button" value="night" onclick="
  nightDayhandler(this);
">
</body>
</html>
'''.format(title=pageId,desc=description,listStr=listStr))
