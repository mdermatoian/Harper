f = open("p3d.txt", "r")

sumofbonus = 0

lastname = str(f.readline().rstrip('\n'))

while lastname != "":
  salary = float(f.readline())

  if salary >= 100000:
    br = .2
  elif salary > 50000 and salary < 100000:
    br = .15
  else:
    br = .1

  bonus = salary * br
  sumofbonus = sumofbonus + bonus

  print("Last Name:    ", lastname)
  print("Salary:       ", salary)
  print("Bonus:        ", bonus)

  lastname = str(f.readline().rstrip('\n'))

print("*****")
print("Sum of Bonus: ", sumofbonus)