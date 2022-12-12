class Employee:

  def __init__ (self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  def bonus(self, rate):
    b = float(rate) * float(self.pay)
    return b

empl1 = Employee('Matt', 'DerMatoian', 60000.00)

print(empl1.email)
print(empl1.first)
print(empl1.last)
print("Employee Salary: ", empl1.pay)
print("Bonus with a Bonus Rate of 10%:", empl1.bonus(0.10))
print("Bonus with a Bonus Rate of 20%:", empl1.bonus(0.20))