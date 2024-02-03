#This is simple python code for finding factorial of number entered by the user
n=int(input("Enter the number whose factorial you want to find: "))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(f"The factorial of enterred number is {fact(n)}")
