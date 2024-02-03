#This is simple python code for finding factorial of number entered by the user
n=int(input("Enter the number whose factorial you want to find: "))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(f"The factorial of enterred number is {fact(n)}")

#This is simple python code for adding numbers from 1 to entered number by user
u=int(input("Enter the number of your choice: "))
sum=0
for i in range(1,u+1):
    sum=i+sum
print(f"The sum of numbers from one to entered number is {sum}")

