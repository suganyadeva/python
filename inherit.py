#PROGRAM TO PERFORM INHERITANCE
class student:
 name="xxx"
 mark=90
 def display(self):
  print("student name is {0}\n student mark is {1}".format(self.name,self.mark))
class sports(student):
 game="cricket"
 rank=2
 def play(self):
  print("play game",self.game)
  print("rank",self.rank)
s=sports()
s.display()
s.play()
