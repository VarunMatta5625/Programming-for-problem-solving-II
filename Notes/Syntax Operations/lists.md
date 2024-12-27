# Lists


---



---

For example, <br>
``` 
student = ["varun","20204005625","vmatta@student.gitam.edu"]

print(student)
```
Outputs to: <br>
`['varun', '20204005625', 'vmatta@student.gitam.edu']`

If we use a loop to print the elements individually 
```
for i in student:
    print(i,end = " ")
```
Outputs to:<br>
`varun
20204005625
vmatta@student.gitam.edu`

---
Let's see how each element is stored as inside of the list
```
for i in student:
    print(type(i),end = " ")
```
Outputs to: <br>
`<class 'str'>
<class 'str'>
<class 'str'>`

Alternatively in the previous array `a` 

```
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    print(type(i,end=" ")
```
Outputs to: <br>
`<class 'int'> <class 'int'> <class 'int'> <class 'int'> <class 'int'> <class 'int'> <class 'int'> <class 'int'> <class 'int'> `
<br>
<br> This is only a one dimensional list, let us have a look at 2 - dimensional array

# 2D Lists
Let's start with an example 
``` 
student = [ ["varun","20204005625","vmatta@student.gitam.edu"],
["Pavan","2024031739","ptumu@student.gitam.edu"] ]

for i in student:
    print(i)
```
Outputs to:<br>
`['varun', 20204005625, 'vmatta@student.gitam.edu']` <br>
`['Pavan', 2024031739, 'ptumu@student.gitam.edu']`