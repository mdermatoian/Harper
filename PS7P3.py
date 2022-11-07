def compmpg(miles, gallons):
  mpg = miles / gallons

  return mpg

def compcost(gallons):
  cost = gallons * 2.5

  return cost

city = input("Enter Destination City: ")
miles = float(input("Enter Miles Travelled: "))
gallons = float(input("Enter Amount of Gallons Used: "))

mpg = compmpg(miles, gallons)
cost = compcost(gallons)

print("Destination City: ", city)
print("Miles Travelled: ", miles)
print("Miles Per Gallon: ", mpg)
print("Total Cost of Gas: ", cost)