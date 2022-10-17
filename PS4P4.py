qty = int(input("Quantity: "))

if qty >= 25:
  ppt = 50
elif qty >= 10 and qty <= 24:
  ppt = 60
elif qty >=5 and qty <=9:
  ppt = 70
else:
  ppt = 75

total = qty * ppt

print("Quantity: ", qty)
print("Price Per Ticket: ", ppt)
print("Total: ", total)