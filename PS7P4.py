def comprate(code):
  if code == "L":
    rate = 25
  elif code == "A":
    rate = 30
  elif code == "J":
    rate = 50

  return rate

def compgrosspay(hrs, rate):
  grosspay = hrs * rate

  return grosspay

name = input("Enter Last Name: ")
code = input("Enter Job Code: ")
hrs = float(input("Enter Hours Worked: "))

rate = comprate(code)
grosspay = compgrosspay(hrs, rate)

print(name, "Grosspay is ", grosspay)