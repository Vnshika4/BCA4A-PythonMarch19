print("Name: Vanshika")
print("Roll No. 2210997266")

sales = int (input("Enter Sales Amount :"))

if ( sales >= 15000 ):
    commission = sales * 0.2
    
elif ( sales >= 1000 ):
    commission = sales * 0.15
    
else :
    commission = sales * 0.1 
    
print (commission)
