#PROGRAM FOR MATRIX MULTIPLICATION
Sa=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]
c=0
for i in range(3):
 for j in range(3):
  for k in range(3):
   c+=a[i][j]*b[j][i]
  print(" "+str(c),end=' ')
 print()
