def compprice(miles):
  if miles >= 30:
    price = 12
  elif miles > 20 and miles < 30:
    price = 10
  elif miles > 10 and miles < 20:
    price = 8
  else:
    price = 5

  return price
response = input("Do you want to find out the cost of your tickets?(Yes or No) ")

sumprice = 0

while response == "Yes":
  name = input("Enter Last Name: ")
  miles = int(input("Enter Miles from downtown Chicago: "))

  price = compprice(miles)
  sumprice = sumprice + price

  print("Price of last ticket: ", price)
  print("Price of all tickets: ", sumprice)

  response = input("Do you want to add another ticket?(Yes or No) ")
