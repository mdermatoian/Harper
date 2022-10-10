b = float(input("Number of Books to Order: "))
c = float(input("Cost Per Book: "))

t = b*c

if t>50:
  s = 0.00
else:
  s = 25.00

print("Order Total ", t)
print("Shipping Cost ", s)