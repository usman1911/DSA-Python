n = int(input("Enter Number: "))

i = 0
while i < n:
    if i%2 == 0:
        print ("0", end="")
    else:
        print ("*" , end="")
        
    i+=1
        
print()