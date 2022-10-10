l = input("Last Name: ")
d = float(input("Number of Dependents: "))
g = float(input("Gross Income: "))

ag = g - (d * 12000)

if ag>50000:
  t = .2
else:
  t = .1

it = ag * t

if it<0:
  it = 100

print("Last Name: ", l)
print("Gross Income: ", g)
print("Number of Dependents: ", d)
print("Adjusted Gross Income: ", ag)
print("Income Tax: ", it)