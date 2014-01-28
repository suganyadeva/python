#TO CREATE A FORM BY USING PYTHON 
#!python33/python
import cgi,cgitb
cgitb.enable()
print("content-type:text/html")
print("")
f=cgi.FieldStorage()
n=f.getvalue('uname')
k=eval(f.getvalue('reg'))
l=eval(f.getvalue('mark'))
print("hi{0},welcome to python\n".format(n))
print("<br>")
print(your regno is:{0}\n".format(k))
print("<br>")
if(l>=40):
 print("you passed")
else:
 print(you failed")
