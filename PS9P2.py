def comppoints (s1, s2, s3):
  total = s1 + s2 + s3
  avgscore = total / 3
  return total, avgscore






name = input("Enter Last Name: ")
s1 = float(input("Enter Exam Score 1: "))
s2 = float(input("Enter Exam Score 2: "))
s3 = float(input("Enter Exam Score 3: "))

total, avgscore = comppoints(s1, s2, s3)

print("Last Name: ", name)
print("Exam Score Average", avgscore)
print("Total Points: ", total)