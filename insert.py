#to insert a row in a table
import mysql.connector
cn=mysql.connector.connect(user='root',database='student',password='root')
cr=cn.cursor()
cr.execute("insert into list(regno,name,mark,result)values({0},'{1}',{2},'{3}')".format(3,'ccc',30,'fail'))
cn.commit()
print("record created")
cr.close()
cn.close()
#to view the table directly
cn=mysql.connector.connect(user='root',database='student',password='root')
cr=cn.cursor()
cr.execute("select * from list")
for(r,n,m,rs) in cr:
 print("{0:<5}|{1:^20}|{3:>10}|".format(r,n,m,rs))
cr.close()
cn.close()
