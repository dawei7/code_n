# Product of the Last K Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1352 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Design, Data Stream, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [product-of-the-last-k-numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/product-of-the-last-k-numbers/).

### Goal
Design a stream structure that appends numbers and returns the product of the last `k` appended numbers.

### Function Contract
**Inputs**

- `operations`: method calls written as `[method, args]` pairs using `add` and `getProduct`.

**Return value**

List of method results. `add` returns `None`; `getProduct(k)` returns the requested product.

### Examples
**Example 1**

- Input: `operations = [["add", [3]], ["add", [0]], ["add", [2]], ["add", [5]], ["add", [4]], ["getProduct", [2]], ["getProduct", [3]], ["getProduct", [4]], ["add", [8]], ["getProduct", [2]]]`
- Output: `[null, null, null, null, null, 20, 40, 0, null, 32]`

**Example 2**

- Input: `operations = [["add", [1]], ["add", [2]], ["add", [3]], ["getProduct", [3]]]`
- Output: `[null, null, null, 6]`

**Example 3**

- Input: `operations = [["add", [0]], ["add", [9]], ["getProduct", [1]], ["getProduct", [2]]]`
- Output: `[null, null, 9, 0]`

---

## Solution
### Approach
Prefix products with zero reset.

### Complexity Analysis
- **Time Complexity**: `O(1)` per operation.
- **Space Complexity**: `O(n)` for values since the most recent zero.

### Reference Implementations
<details>
<summary>python</summary>

```python
class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]


def solve(operations):
    product = ProductOfNumbers()
    output = []
    for operation, args in operations:
        if operation == "add":
            output.append(product.add(args[0]))
        elif operation == "getProduct":
            output.append(product.getProduct(args[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
```
</details>
