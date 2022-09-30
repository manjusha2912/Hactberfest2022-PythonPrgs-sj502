def bigNum(n1,n2,n3):
    if (n1>n2 and n1>n3):
        print(n1,",the first, is the greatest.")
    elif (n2>n1 and n2>n3):
        print(n2,",the second, is the greatest.")
    else:
        print(n3,",the third, is the greatest.")
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
bigNum(n1,n2,n3)
