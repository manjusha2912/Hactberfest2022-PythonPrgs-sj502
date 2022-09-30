def divBy2(num):
    if num % 2 == 0:
        print(num,"is divisible by two. Hence, it is even.")
    else:
        print(num,"is not divisible by two. Hence, it is odd.")
num = int(input("Enter number to be checked: "))
divBy2(num)
