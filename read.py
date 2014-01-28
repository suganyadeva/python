#PROGRAM TO READ A FILE
f=open("d:/python/text.txt","r")
str=f.read()
print(str)
print(f.name)
print(f.mode)
print(f.closed)
