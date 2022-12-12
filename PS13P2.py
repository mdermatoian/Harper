class Student:
  def __init__(self, first, last, credits):
    self.first = first
    self.last = last
    self.credits = credits

  def owed(self, code):
    if code == "I":
      owed = 250 * self.credits
    else:
      owed = 500 * self.credits
    return owed

stu1 = Student('Matt', 'DerMatoian', 10)

print(stu1.first)
print(stu1.last)
print("Credits: ", stu1.credits)
print("Tuition Owed If Code I: ", stu1.owed('I'))
print("Tuition Owed If Code Not I: ", stu1.owed('O'))