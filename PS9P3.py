def sales_report(sales):
  if sales > 100000:
    commrate = .1
  else:
    commrate = .05

  comm = commrate * sales
  target = sales * 1.05

  return comm, target

name = input("Enter Last Name: ")
sales = float(input("Enter Sales Amount: "))
comm, target = sales_report(sales)

print("Commision: ", comm)
print("Next Year's Target: ", target)