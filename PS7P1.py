def comptotal(qty, price):
  total = float(qty) * float(price)

  if total > 10000.00:
    total = total * .9
  else:
    total = total

  return total

qty = float(input("Enter Quantity: "))
price = float(input("Enter Price: "))

total = comptotal(qty, price)

print("Total is $", total)
print("Quantity is: ", qty)
print("Price is: ", price)