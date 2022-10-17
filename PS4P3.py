pr = int(input("Principle Amount: "))
ytm = int(input("Years to Maturity: "))

if pr > 100000 and ytm == 5:
  ir = .06
elif pr <= 100000 and pr >= 50000 and ytm == 10:
  ir = .05
elif pr <= 100000 and pr >= 50000 and ytm == 5:
  ir = .04
else:
  ir = .02

fyi = pr * ir

print("Principle Amount: ", pr)
print("Interest Rate: ", ir)
print("Interest Amount for First Year: ", fyi)