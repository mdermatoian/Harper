def hilow (lastn, score):
  l = len(lastn)
  hiscore = -1
  lowscore = 999
  for y in range (0, l, 1):
    if float(score[y]) > float(hiscore):
      hiindex = y
      hiscore = score[y]

    if float(score[y]) < float(lowscore):
      lowindex = y
      lowscore = score[y]

  print("Highest Score: ", lastn[hiindex], score[hiindex])
  print("Lowest Score: ", lastn[lowindex], score[lowindex])

def displaynames(lastn, score):
  for i in lastn, score:
    print(i)
  for y in score:
    print(y)

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

def rdisplaynames(lastn):
  l = len(lastn)
  print("Last Names in Reverse Order: ")
  for y in range (l-1, -1, -1):
    print(lastn[y])


hilow(lastn, score)