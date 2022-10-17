name = input("Last Name: ")
sal = int(input("Salary: "))
level = int(input("Job Level: "))

if level >= 10:
  br = .25
elif level <=9 and level >=5:
  br = .20
else:
  br = .10

bonus = sal * br

print("Last Name: ", name)
print("Bonus: ", bonus)