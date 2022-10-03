#comment input
p = float(input("Enter The Price: "))
d = float(input(" Enter The Discount Percentage: "))

#comment process
t = p * (d * 0.01)
a = p - t

#output
print("Discount Amount Equals ", t)
print("Discount Price Equals", a)