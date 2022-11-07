nooforders = 0
sumofdiscamt = 0

response = input("Do you want to calculate total order with discount? (Yes or No): ")

while response == "Yes":
  qty = float(input("Input Quantity: "))
  price = float(input("Input Price: "))
  extprice = qty * price
  if extprice > 10000.00:
    discamt = extprice * 0.25
  else:
    discamt = extprice * 0.10
  totalorder = extprice - discamt
  sumofdiscamt = sumofdiscamt + discamt
  nooforders = nooforders + 1
  print("Extended Price is $", extprice)
  print("Discount Earned $", discamt)
  print("Total Order Amount $", totalorder)
  response = input("Do you want to enter another order? (Yes or No): ")

print("Total Discounts Given $", sumofdiscamt)
print("Number of orders entered: ", nooforders)
