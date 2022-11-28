def displaynames(lastn, score):
  print("Names in Order: ")
  l = len(lastn)
  for x in range(0, l, 1):
    print(lastn[x], "  ", score[x])


f = open("PS10(1-3).txt")

lastname = f.readline()
lastn = []
score = []

while lastname != "":
  lastn.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  score.append(s)
  lastname = f.readline()

f.close
displaynames(lastn, score)

def rdisplaynames(lastn):
  l = len(lastn)
  print("Names in Reverse Order: ")
  
  for x in range(l-1, -1, -1):
    print(lastn[x], "  ", score[x])

rdisplaynames(lastn)