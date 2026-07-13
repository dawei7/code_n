# Find Xor-Beauty of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2527 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-xor-beauty-of-array](https://leetcode.com/problems/find-xor-beauty-of-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-xor-beauty-of-array/).

### Goal
Given an array of integers, calculate the "Xor-beauty" of the array. The Xor-beauty is defined as the result of the expression `((nums[i] | nums[j]) & nums[k])` XORed across all possible triplets `(i, j, k)` where `0 <= i, j, k < n`.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the cumulative XOR sum of the bitwise operations performed on all triplets.

### Examples
**Example 1**

- Input: `nums = [1, 4]`
- Output: `5`

**Example 2**

- Input: `nums = [15, 45, 20, 2, 34, 35, 5, 44, 32, 30]`
- Output: `34`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`

---

## Solution
### Approach
The problem relies on the properties of the XOR operation and the distributive nature of bitwise operators. By expanding the expression `(nums[i] | nums[j]) & nums[k]` and considering the XOR sum over all `i, j, k`, terms where the same index appears an even number of times cancel out due to the property `x ^ x = 0`. Mathematically, this simplifies the entire expression to the XOR sum of all elements in the array: `nums[0] ^ nums[1] ^ ... ^ nums[n-1]`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array exactly once to compute the XOR sum.
- **Space Complexity**: `O(1)`, as we only use a single variable to store the running XOR result.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List
from functools import reduce
from operator import xor

def solve(nums: List[int]) -> int:
    """
    Calculates the Xor-beauty of the array.
    The expression ((nums[i] | nums[j]) & nums[k]) XORed over all i, j, k
    simplifies to the XOR sum of all elements in the array.
    """
    return reduce(xor, nums)
```
</details>
