def compba(hits, atbats):
  ba = hits / atbats

  return ba


name = input("Enter Last Name: ")
hits = float(input("Enter Number of Hits: "))
atbats = float(input("Enter Number of At Bats: "))

ba = compba(hits, atbats)

print(name,"Batting Average is: ", ba)