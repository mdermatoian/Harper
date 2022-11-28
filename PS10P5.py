def displaynames(lastn, ba):
  l = len(lastn)
  for x in range(0, l, 1):
    print(lastn[x], "  ", ba[x])


f = open("PS10(4-5).txt")

lastname = f.readline()
lastn = []
ba = []

while lastname != "":
  lastn.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  ba.append(s)
  lastname = f.readline()

f.close
displaynames(lastn, ba)

def seqsearch(lastn, sname):
  l = len(lastn)
  sindex = -1
  for y in range (0, l, 1):
    if lastn[y] == sname:
      sindex = y

  return sindex

response = input("Do You Want To Find Out A Player's Batting Average? (Yes or No): ")

while response == "Yes":
  sname = input("Enter Last Name to Find Batting Average For: ")
  i = seqsearch(lastn, sname)
  if i == -1:
    print("Name Not Found")
  else:
    print(lastn[i], "Batting Average of", ba[i])

  response = input("Do You Want To Find Out A Player's Batting Average? (Yes or No): ")