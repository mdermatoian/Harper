def b_average (s1, s2, s3, hand):
  avg = (s1 + s2 + s3) / 3
  avghand = ((s1 + s2 + s3) + (hand * 3)) / 3
  return avg, avghand




name = input("Enter Last Name: ")
s1 = float(input("Enter 1st Score: "))
s2 = float(input("Enter 2nd Score: "))
s3 = float(input("Enter 3rd Score: "))
hand = float(input("Enter Handicap: "))

avg,avghand = b_average (s1, s2, s3, hand)

print("Last Name: ", name)
print("Average Score: ", avg)
print("Average Score With Handicap: ", avghand)