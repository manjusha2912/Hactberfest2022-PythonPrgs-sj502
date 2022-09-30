def calculate(n1,n2,op):
    if op=="+":
        print(n1,"+",n2,"=",n1+n2)
    elif op=="-":
        print(n1,"-",n2,"=",n1-n2)
    elif op=="*":
        print(n1,"*",n2,"=",n1*n2)
    elif op=="/":
        print(n1,"/",n2,"=",n1/n2)
    else:
        print("Invalid response recieved.")

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
op=input("Enter the operator {+,-,*,/}: ")
calculate(n1,n2,op)
