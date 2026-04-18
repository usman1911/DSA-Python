n = int(input("Enter the number: "))
if n%2 == 0:
    print("even")
    if n%2 != 0 and n%3 ==0:
        print("divisible by 3")
    if n%2 != 0 and n%3 !=0:
        print("not divisible by 3")