#PYTHON PROGAM FOR PERMUTATION OF TWO NUMBERS

# Factorial function
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact
    
# Permutation function    
def permutation(n,r):
    numerator=factorial(n)
    denominator=factorial(n-r)
    perm=numerator/denominator
    print("The permutation of P(",n,",",r,") is ", perm)
    return perm

# Driver program to test above function
n=6
r=2
permutation(n,r)

# User input 
uch=input("Do you want to try? y/n: ")
if uch=="y" or uch=="Y":
    n=int(input("Enter value of n: "))
    r=int(input("Enter value of r: "))
    permutation(n,r)
