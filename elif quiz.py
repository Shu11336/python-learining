#pizza shop
print("welcome to pizza shop")
size = input("S, M OR L")
pepperoni = input("do you want pepperoni, Y OR N")
cheese = input("do you want extra cheese?, Y OR N")
#small price= 15
#meduim price= 20
#large price= 25
#p price=5
#c price =2

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("Wrong Size value")

if pepperoni == "Y":
    bill += 5
else:
    print("no pepperoni added")

if cheese == "Y":
    bill += 2
else:
    print("no cheese added")
print(f"your bill is {bill}")



