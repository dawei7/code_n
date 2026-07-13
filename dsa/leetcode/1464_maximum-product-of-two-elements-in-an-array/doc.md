# Maximum Product of Two Elements in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1464 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-product-of-two-elements-in-an-array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/).

### Goal
Choose two distinct numbers and maximize `(a - 1) * (b - 1)`.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

The maximum product after subtracting `1` from each chosen value.

### Examples
**Example 1**

- Input: `nums = [3,4,5,2]`
- Output: `12`

**Example 2**

- Input: `nums = [1,5,4,5]`
- Output: `16`

**Example 3**

- Input: `nums = [10,2,5,2]`
- Output: `36`

---

## Solution
### Approach
Track the two largest values in one pass, then compute their adjusted product.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums):
    first = second = float("-inf")
    for num in nums:
        if num > first:
            first, second = num, first
        elif num > second:
            second = num
    return (first - 1) * (second - 1)
```
</details>
