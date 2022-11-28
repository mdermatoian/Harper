def displaynames(lastn):
  print("Names in Order: ")
  for i in lastn:
    print(i)


f = open("PS10(1-3).txt")

lastname = f.readline()
lastn = []

while lastname != "":
  lastn.append(str(lastname).rstrip("\n"))
  lastname = f.readline()

displaynames(lastn)

def rdisplaynames(lastn):
  l = len(lastn)
  print("Names in Reverse Order: ")
  for y in range (l-1, -1, -1):
    print(lastn[y])


rdisplaynames(lastn)