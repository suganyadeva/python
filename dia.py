#PROGRAM TO GET A DIAMOND SHAPE
a=eval(input("enter a value"))#to get the value and print
for i in range(a):
 for j in range(i,a):
  print(" ",end='')
 for k in range(i):
  print(" *",end='')
 print()
for i in range(a):
 for j in range(i):
  print(" ",end='')
 for k in range(i,a):
  print(" *",end='')
 print()
