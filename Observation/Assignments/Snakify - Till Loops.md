# Input, print and numbers
---

#### 1) Sum of three numbers

Program: 
```
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```

the above program accepts 3 numbers from the user using the builtin function `input()`. It then prints the calculated sum of those 3 numbers

#### 2)Hi John
Program:
```
a = input()
print("Hi "+a)
```
this program accepts the name from the user and greets them with `hi` 

#### 3)Square 
program:
```
a  = int(input())
print(a*a)
```
this program accepts a number and prints its calculated square

#### 4) Area of right angle triangle
program: 
```
b = int(input())
h = int(input())
area = float(0.5*b*h)
print(area)
```
this program accepts base and height of a triangle and calculates the area and prints that value.

#### 5)Hello, Harry!
program:
```
name = input()
print("Hello, " + name + "!")
```
this program accepts a name from the user and greets them `hello` followed by the given name and then an exclamation `!`

#### 6)Apple sharing
program:
```
n = int(input())
k = int(input())


print(k // n)
print(k % n)
```
this program accepts 2 numbers, and divides them, prints their integer quotient. It also performs modulo operation and prints the output remainder.

#### 7)Previous and next
program: 
```
a = int(input())
print('The next number for the number ' + str(a) + ' is ' + str(a + 1) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(a - 1) + '.')
```

this program accept a number and prints its previous number and next.

#### 8)Two timestamps
program:
```
h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = (h1*3600) + (m1*60) + (s1)
t2 = (h2*3600) + (m2*60) + (s2)

print(t2-t1)
```
