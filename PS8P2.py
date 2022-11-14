def compsqf(length, width, height):
  sqf = (2 * length * width) + (2 * length * height) + (2 * width * height)

  return sqf

response = input("Do you want to calculate how many gallons needed? (Yes or No)? ")

while response == "Yes":
  length = float(input("Enter Length: "))
  width = float(input("Enter Width: "))
  height = float(input("Enter Height: "))

  gallons = compsqf(length, width, height)

  print("Gallons Needed: ", gallons)

  response = input("Do you want to calculate how many gallons needed? (Yes or No)? ")