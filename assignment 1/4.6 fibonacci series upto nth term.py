print("Name: Vanshika")
print("Roll No. 2210997266")

n = int (input("Enter the value of n: "))
a,b = 0,1
count = 0
while count < n :
    print(a)
    nth = a + b
    a = b
    b = nth 
    count += 1
    