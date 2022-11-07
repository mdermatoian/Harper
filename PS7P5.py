def comptuition(hrs, code):
  if code == "I":
    cph = 250
  elif code == "O":
    cph = 550

  tuition = hrs * cph

  return tuition

name = input("Enter Last Name: ")
hrs = float(input("Enter Amount of Credit Hours: "))
code = input("Enter Disctrict Code: ")

tuition = comptuition(hrs, code)

print(name, "Tuition is ", tuition)