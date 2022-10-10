n = input("Name of Appliance: ")
c = float(input("Cost of Appliance: "))

if c>1000:
  w = .1
else:
  w = .05

wc = w * c
t = wc + c

print("Appliance: ", n)
print("Cost of Appliance: ", c)
print("Warrantee Cost: ", wc)
print("Total: ", t)