def compavalue(county, mvalue):
  if county == "Cook":
    value = .9
  elif county == "DuPage":
    value = .8
  elif county == "McHenry":
    value =.75
  elif county == "Kane":
    value = .6
  else:
    value = .7

  avalue = mvalue * value

  return avalue

response = input("Do you want to see the Assessed Value of a home?(Yes or No) ")

summvalue = 0
sumavalue = 0

while response == "Yes":
  county = input("Enter County: ")
  mvalue = int(input("Enter Market Value: "))

  avalue = compavalue(county, mvalue)
  summvalue = summvalue + mvalue
  sumavalue = sumavalue + avalue

  response = input("Do you want to add another home?(Yes or No) ")

print("Sum of Market Value is: ", summvalue)
print("Sum of Assessed Value is: ", sumavalue)