def matrixmul(a,b):
 for i in range(3):
  for j in range(3):
   for k in range(3):
    c=a[i][j]+b[j][i]
   print(" ",c,end='')
  print("\n")
