#PROGRAM TO DISPLAY THE TRIANGLE
for i in range(7):
 for j in range(i,7):
  print(" ",end='') 
  for k in range(i):
   if(i==0 or j==0 or i==6 or j==6):
    print(" *",end='') 
 print()
