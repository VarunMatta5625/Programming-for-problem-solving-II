# Lists
lists are ordered, mutable sequence of items enclosed in `[]` <br>
<mark>They can contain data from different datatypes</mark>.
---

A list can be declared simply as shown below <br>
```
a = [] 
a = [1,2,3,4,5,6,7,8,9]
```
A list can contain items from different datatypes<br>

To find the data type of `a` , we can use `type()` function.
```
print(type(a))
```
which prints `<class 'list'>`, classifying it as a <mark> **list</mark>**

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
<br>Clearly all the elements inside a list is stored as strings.
<br> This is only a one dimensional list, let us have a look at 2 - dimensional array

# 2D Lists
Let's start with an example 
```
student = [["varun","20204005625","vmatta@student.gitam.edu"]]

print(student)
```