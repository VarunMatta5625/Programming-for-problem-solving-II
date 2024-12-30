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

---

# Tuple
Tuple can be created like `tup_1 = ()`
<br>Tuple's are NOT mutable<br>
These are compatible with heterogenous type of data and this tuple is close to a **list ()** 
<br> Tuple is hashable
<br>Again these are ordered and indexed <br>
`a = (2)` is **int** but `a = (2,)` is a **tuple** <br>
More such can be stored like `a = (2,2.3,'a', "vinyl")`

---

# Set
can be created as `s_1 = set()` <br>
**sets are not ordered hence cannot be indexed**
<br> sets can be assigned after creating by ` s_1 = {23,21,25,76}`. <br>
sets cannot be `id()`ed
<br> Are sets mutable? <br>
Sets are non-redundant, a.k.a will remove repeated elements.<br>
Sets are not hashable, but only hashable objects can be elements of sets. Hence lists cannot be a part of sets, but tuples can be.

---

# Dictionary - dict
Dicts can be indexed using key value
<br> can be declared using `d_1 = {1:"Distance", 2:"Car"}` and `1` is the key value for `Distance`



---
# To summarize the above
| Collection  | isHeterogeneous | isIndexed | isOrdered | IsMutable | isHashable | Allows Duplicates |
| :---------- | :-------------: | :-------: | :-------: | :-------: | :--------: | :---------------: |
| Lists       | ✅              | ✅        | ✅        | ✅        | ❌         | ✅                |
| Tuple       | ✅              | ✅        | ✅        | ❌        | ✅         | ✅                |
| Set         | ✅              | ❌        | ❌        | ✅        | ❌         | ❌                |
| Dictionary  | ✅              | ✅        | ✅        | ✅        | Keys: ✅   | ❌                |

[What does it mean to be Hashable?](./Hash.md)

---
# Footnotes
[^1]: The number `-1` will indicated the last element 
[^2]: Mutable means the address is retained when the object is changed.

