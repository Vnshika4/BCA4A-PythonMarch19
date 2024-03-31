print("Name: Vanshika")
print("Roll No. 2210997266")

p = int (input("Enter Principal : "))
t = int (input("Enter Time : "))
r = int (input("Enter Rate : "))

Amount = p * (pow((1+r/100),t))
ci = Amount - p
print("Compound Interest is : ", ci)