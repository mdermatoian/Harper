response = (input("Would You Like to continue? (Yes or No): "))

noofstudents = 0

while response == "Yes":
  lastname = (input("Enter Your Last Name: "))
  examscore1 = float(input("Enter Your First Exam Score: "))
  examscore2 = float(input("Enter Your Second Exam Score: "))
  avgscore = (examscore1 + examscore2) / 2
  noofstudents = noofstudents + 1
  print("Exam Average for", lastname)
  print("is", avgscore)
  response = input("Would You Like To Continue? (Yes or No): ")

print("Number of Students Entered: " , noofstudents)