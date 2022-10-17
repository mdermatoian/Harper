partno = int(input("Part Number: "))
qty = input("Quantity to Purchase: ")

if partno == 10 or partno == 55:
  unitprice = 1.00
elif partno == 99:
  unitprice = 2.00
elif partno == 80 or partno == 70:
  unitprice = 3.00
else:
  unitprice = 5.00

total = float(qty) * unitprice

print("Part Number: ", partno)
print("Unit Price: ", unitprice)
print("Total: ", total)