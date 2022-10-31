response = input("Do You Want To Calculate Interest? (Yes or No) ")

while response == "Yes":
  p = float(input("Enter Amount To Invest: "))
  rate = float(input("Enter Interest Rate: "))
  totalint = 0
  print("Year  Beg Bal  End Bal")
  for year in range (1,6,1):
    intamt = p * rate
    endbal = p + intamt
    print(year, "  ", p, "  ", endbal)
    totalint = totalint + intamt
    p = endbal

  print("Total Interest Earned: ", totalint)
  response = input("Do You Want To Calculate Interest? (Yes or No) ")