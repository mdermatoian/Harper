i = input("Enter Item ")
q = float(input("Enter Quantity "))

if i=="A":
  p = 10.00
else:
  p = 20.00

extp = q*p

print("Item: ", i)
print("Unit Price: ", p)
print("Extended Price: ", extp)