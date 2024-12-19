n = int(input("Enter the number of numbers required \n"))

sum = 0 
for i in range(1,n+1):
    sum = sum + i

print(f"The sum of {n} natural numbers is {sum}")