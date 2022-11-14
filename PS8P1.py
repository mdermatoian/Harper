def compfsales(month, sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    forecast = .1
  elif month == "Apr" or month == "May" or month == "Jun":
    forecast = .15
  elif month == "Jul" or month == "Aug" or month == "Sep":
    forecast = .2
  else:
    forecast = .25

  fsales = forecast (1 + forecast)

  return fsales
  
response = input("Would you like to compute next month's sales?(Yes or No) ")

while response == "Yes":
  name = input("Enter Last Name: ")
  month = input("Enter Month (First 3 letters, ex: Jan): ")
  sales = float(input("Enter Sales: "))

  print("Next Month's Sales: ", compfsales(month, sales))

  response = input("Would you like to compute next month's sales?(Yes or No) ")