response = input("Would You Like To Continue? (Yes or No): ")

sumgrosspay = 0
noofemp = 0

while response == "Yes":
  lastname = input("Enter Last Name: ")
  hours = float(input("Enter Hours Worked: "))
  rate = float(input("Enter Hourly Rate: "))
  if hours >= 40:
    grosspay = (40 * rate) + (((hours - 40) * 1.5) * 40)
  else:
    grosspay = rate * hours

  noofemp = noofemp + 1
  sumgrosspay = sumgrosspay + grosspay
  print("Grosspay: ", grosspay)
  response = input("Would You Like To Continue? (Yes or No): ")
  
avggrosspay = sumgrosspay / noofemp
print("Sum of Gross Pay $", sumgrosspay)
print("Number of Employees Entered: ", noofemp)
print("Average Gross Pay $", avggrosspay)