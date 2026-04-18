n = int(input("Enter the number:"))
for i in range(n):
    if i%2 == 0:
        print("0" , end="")
    else:
        print("*" , end="")
print()