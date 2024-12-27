# Functions
In mathematical functions,a relationship is defined between one variable (the independent variable) and another variable (the dependent variable).

But in computer programming functions are specific blocks of code that are written to accomplish a defined task , by taking a value(s) in and producing an output(s).

## Library Functions
### 1) print() <br>
The print function in python can consist of the following <br>
`print(*objects, sep=' ', end='\n', file=None, flush=False)`<br>
- Here, if observed properly, the `print()` statement, by default comes with a separation of a single whitespace. <br>
- It also executes and proceeds to the next line (by default) <br> 
---------
#### `+` Operator usage
Two strings can be concatenated by using `+` operator within the `print()` function.
<br> <br>
For example, <br>
```
print("Hello"+"World")
```
Outputs to,  
>HelloWorld 
---------
#### `,` operator usage
Two objects can be printed sequentially, by using `+` operator within the `print()` function.<br>
- This by default comes with a single white space (separator)
For example, <br>
```
print("Hello","World")
```
Outputs to,  
>Hello World
>
<br> <br> 
---
<br> <br>
### 2) type() <br>
The type function consists of the following, <br>
`type(object)` <br>
returns the type of data stored in the objects or variables that is passed along as argument. <br>
For example,  <br>

 ```
a = 65
b = int(a)
c = chr (a)

print(type(a))
print(type(b))
print(type(c))
```
Outputs to, <br>
`<class 'int'>`<br>
`<class 'int'>`<br>
`<class 'str'>`<br>

<br>

`type()` can also be used to identify lists
```
a = []
print(type(a))
```

Outputs to, <br>
`<class 'list'>`
