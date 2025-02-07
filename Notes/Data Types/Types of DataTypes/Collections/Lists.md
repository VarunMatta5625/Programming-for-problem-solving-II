# List
**Lists are ordered, mutable sequences of items enclosed in `[]`.** <br>
Lists can be indexed, using either positive or negative indices [^1]. <br>
Lists can be concatenated using the `+` operator, and upon concatenation, the id remains the same, making it <mark>mutable </mark>[^2].

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
which prints `<class 'list'>`, classifying it as a **list**



# Footnotes
[^1]: The number `-1` will indicated the last element
[^2]: Mutable means the address is retained when the object is changed. 