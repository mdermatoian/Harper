def compmsrp(msrp, make, model, code):
  if make == "Honda" and model == "Accord":
    off = .1
  elif make == "Toyota" and model == "Rav4":
    off = .15
  elif code == "Y":
    off = .3
  else:
    off = .05

  newmsrp = msrp - (off * msrp)

  return newmsrp

response = input("Do you want to calculate the MSRP and sales price of a car? (Yes or No) ")

sumnewmsrp = 0
sumdprice = 0

while response == "Yes":
  make = input("Enter Make: ")
  model = input("Enter Model: ")
  code = input("Enter Electric Vehicle Code (Y or N): ")
  msrp = float(input("Enter MSRP: "))

  newmsrp = compmsrp(msrp, make, model, code)
  dprice = newmsrp + (.07 * newmsrp)
  sumnewmsrp = sumnewmsrp + newmsrp
  sumdprice = sumdprice + dprice

  response = input("Do you want to calculate the MSRP and sales price of another car? (Yes or No) ")

print("Sum of all MSRP's: ", sumnewmsrp)
print("Sum of all Sales Prices: ", sumdprice)