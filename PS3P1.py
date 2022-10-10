qty = float(input("Enter quantity ordered "))

if qty>=1000:
  up = 3.00
else:
  up = 5.00

extprice = qty * up
tax = extprice * 0.07
total = tax + extprice

print("Quantity ordered ", qty)
print("Unity Price $", up)
print("Extended Price $", extprice)
print("Tax $", tax)
print("Total $", total)