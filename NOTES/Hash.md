# Introduction to Hash

A hash value is like a unique ID created for a piece of data.<br>It's a number created by running data (like a name or file) through a special formula called a hash function.

Now the key fact is that, it is deterministic because **the same input always produces the same hash value**.

And at the same time the hash value has a fixed size, regardless of the input siz.

Creating this said **hash value** is called **hashing**.
This can be done by using `hash()`

In python,
The `hash()` function computes the **hash value** for immutable objects like strings, integers, tuples.