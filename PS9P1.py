def discount(qty, price, discrate):
  total = (qty * price)
  discamt = discrate * total
  discprice = total - discamt

  return discamt, discprice




qty = float(input("Enter Quantity: "))
price = float(input("Enter Unit Price: "))
discrate = float(input("Enter Discount Rate: "))
discamt,discprice = discount(qty, price, discrate)

print("Quantity: ", qty)
print("Unit Price: ", price)
print("Discount Amount: ", discamt)
print("Discounted Price: ", discprice)