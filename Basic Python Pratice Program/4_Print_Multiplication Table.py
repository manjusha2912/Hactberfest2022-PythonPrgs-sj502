def mulTable(n,l):
    arr=[]
    for i in range(1,l+1):
        x=n*i
        arr.append(x)
    print(arr)
n=int(input("Enter number for table: "))
l=int(input("Enter last number to be mutiplied: "))
mulTable(n,l)
