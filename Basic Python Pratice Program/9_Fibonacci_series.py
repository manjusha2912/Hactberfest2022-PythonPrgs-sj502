def fibo(n,arr):
    for i in range(n):
        x=arr[i]+arr[i+1]
        arr.append(x)
arr=[1,1]       
n=int(input("Enter number of Fibonacci numbers: "))
fibo(n,arr)
print(arr)
