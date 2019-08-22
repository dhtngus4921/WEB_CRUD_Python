#!C:\Program Files (x86)\Python\Python37-32\python.exe

import cgi,os
form=cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

print("Location: index.py");
print()
