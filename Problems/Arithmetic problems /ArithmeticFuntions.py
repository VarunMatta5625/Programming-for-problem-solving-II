x = int (input ("Enter value of x\n"))
y = int (input ("Enter value of y\n"))


def add (x,y):
    return x+y

def diff (x,y):
    return x-y

def pro (x,y):
    return x*y

def division (x,y):
    return x/y

def quotient (x,y):
    return x//y

def rem (x,y):
    return x%y

print("Operations are:")
print(f'The sum is {add(x,y)}')
print(f'The difference is {diff(x,y)}')
print(f'The product is {pro(x,y)}')
print(f'The quotient (floating point) is {division(x,y):.90f}')
print(f'The quotient is {quotient(x,y)}')
print(f'The remiander when division is performed between {x} and {y} is {rem(x,y)}')
