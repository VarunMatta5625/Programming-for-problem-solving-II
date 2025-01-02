---
# To summarize the above
| Collection  | isHeterogeneous | isIndexed | isOrdered | IsMutable | *isHashable | Allows Duplicates | Sliceable |
| :---------- | :-------------: | :-------: | :-------: | :-------: | :--------: | :---------------: | :-------: |
| Lists       | ✅              | ✅        | ✅        | ✅        | ❌         | ✅                | ✅        |
| Tuple       | ✅              | ✅        | ✅        | ❌        | ✅         | ✅                | ✅        |
| Set         | ✅              | ❌        | ❌        | ✅        | ❌         | ❌                | ❌        |
| Dictionary  | ✅              | ✅        | ✅        | ✅        | Keys: ✅   | ❌                | ❌        |


*[What does it mean to be Hashable?](../Functions()/Library%20Functions/hash().md)


