def comptotal (qty, price):
  total = qty * price
  tax = total * .07
  return tax, total





qty = float(input("Enter Quantity: "))
price = float(input("Enter Price Per Unit: "))

tax, total = comptotal (qty,price)

print("Total is $", total)
print("Tax Cost is $", tax)