year = int (input("Enter a number \n"))

a = (year%4==0) + ((year%4==0) *(year%400 == 0))

print(f"The given year's leap truth value is {a}")