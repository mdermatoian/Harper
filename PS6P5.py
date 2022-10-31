f = open("p5d.txt", "r")

totaltuition = 0
c = 0

lastname = str(f.readline().rstrip('\n'))

while lastname !="":
  dcode = str(f.readline())
  credits = int(f.readline())

  if dcode == "I":
    costpercredit = 250
  else:
    costpercredit = 500

  tuition = costpercredit * credits
  c = c + 1
  totaltuition = totaltuition + tuition

  print("Last Name:          ", lastname)
  print("Amount of Credits:  ", credits)
  print("Tuition:            ", tuition)

  lastname = str(f.readline().rstrip('\n'))

print("*****")
print("Total Tuition:      ", totaltuition)
print("Number of Students: ", c)