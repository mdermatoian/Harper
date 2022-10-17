qty = int(input("Quantity: "))

if qty > 10000:
  price = 10
elif qty <= 10000 and qty >= 5000:
  price = 20
else:
  price = 30

extprice = qty * price
tax = .07 * extprice
total = tax + extprice

print("External Price: ", extprice)
print("Tax: ", tax)
print("Total: ", total)