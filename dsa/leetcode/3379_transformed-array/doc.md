# Transformed Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3379 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [transformed-array](https://leetcode.com/problems/transformed-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/transformed-array/).

### Goal
Given an integer array `nums`, generate a new array `result` of the same length where each element at index `i` is determined by the value at index `(i + nums[i]) % n`, where `n` is the length of the array. If the calculated index is negative, it wraps around correctly using modulo arithmetic.

### Function Contract
**Inputs**

- `nums`: A list of integers where each element represents a jump offset.

**Return value**

- A new list of integers representing the transformed array.

### Examples
**Example 1**

- Input: `nums = [3, -2, 1, 1]`
- Output: `[1, 1, 1, 3]`

**Example 2**

- Input: `nums = [-1, 4, -1]`
- Output: `[-1, -1, 4]`

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `[0, 0, 0]`

---

## Solution
### Approach
The problem is a direct simulation of index mapping. By utilizing the modulo operator `%` in Python, we handle both positive and negative offsets seamlessly, as Python's `%` operator returns a result with the same sign as the divisor (the array length), effectively performing circular array indexing.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array exactly once to compute each new element.
- **Space Complexity**: `O(n)` to store and return the new transformed array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Transforms the array by mapping each index i to the value at (i + nums[i]) % n.
    Python's modulo operator handles negative numbers correctly for circular indexing.
    """
    n = len(nums)
    result = [0] * n

    for i in range(n):
        # Calculate the target index using modulo arithmetic
        # Python's % operator ensures the result is always in [0, n-1]
        target_index = (i + nums[i]) % n
        result[i] = nums[target_index]

    return result
```
</details>
