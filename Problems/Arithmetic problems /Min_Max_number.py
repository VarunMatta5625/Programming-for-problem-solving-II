a = int(input("Enter a number\n"))
b = int(input("Enter another number\n"))

min = int(((a+b) - abs((a-b)))/2)
max = int(((a+b) + abs((a-b)))/2)

print(f"The min number is {min} and the max number is {max}")