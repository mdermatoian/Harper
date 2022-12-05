def dl1 (mylist):
  n = int(input("Number of Items for Your List: "))
  for n in range (0,n,1):
    s = int(input("Enter an Integer: "))
    mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)

#main
mylist = []
mylist = dl1 (mylist)
displaylist(mylist)
print(mylist)
#DL2
mylist.insert(0,99)
print(mylist)
#DL3
mylist[0] = 100
print(mylist)
#DL4
mylist2 = [500, 600, 700, 800, 900]
print(mylist2)
mylist.extend(mylist2)
print(mylist)
#DL5
mylist.remove(800)
print(mylist)
#DL6
mylist.pop(3)
print(mylist)

print("***********************************")

#DL7
mylist3 = ["A", "B", "C", "A", "A", "C"]
print(mylist3)
#DL8
print("Count of 'A' Grades In The List: ", mylist3.count("A"))
#DL9
print("Position of First 'B' Grade: ", mylist3.index("B"))
#DL10

def seqsearch(mylist3):
  l = len(mylist3)
  sindex = -1
  for y in range (0, l, 1):
    if mylist3[y] == sname:
      sindex = y

  return sindex

response = input("Do You Want To See If A Specific Grade is In The List? (Yes or No): ")

while response == "Yes":
  sname = input("Enter Grade To Search For: ")
  i = seqsearch(mylist3)
  if i == -1:
    print("Grade Not Found")
  else:
    print("Grade Found")

  response = input("Do You Want To See If A Specific Grade is In The List? (Yes or No): ")

#DL11
mylist2.clear()
print(mylist2)
#NOTE DL12 IS LAST SO THAT THE ERROR FROM DISPLAYING LIST 2 AFTER DELETING DOESNT STOP THE CODE FROM CONTINUING
#DL13
mylist4 = ["Rizzo", "Davis", "Baez", "Happ", "Bryant"]
print(mylist4)
#DL14
mylist4.sort()
print(mylist4)
#DL15
players2 = mylist4.copy()
print(players2)
#DL16
players2.reverse()
print(players2)
#DL12
del mylist2
print(mylist2)