# Apply Operations to an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2460 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [apply-operations-to-an-array](https://leetcode.com/problems/apply-operations-to-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/apply-operations-to-an-array/).

### Goal
Transform an array of non-negative integers by performing a series of sequential operations: first, iterate through the array and double any element that is equal to its immediate successor while setting the successor to zero. After these operations are complete, shift all non-zero elements to the front of the array while maintaining their relative order, filling the remaining trailing positions with zeros.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers (`List[int]`).

**Return value**

- A new list of integers representing the modified array after the operations are applied.

### Examples
**Example 1**

- Input: `nums = [1, 2, 2, 1, 1, 0]`
- Output: `[1, 4, 2, 0, 0, 0]`

**Example 2**

- Input: `nums = [0, 1]`
- Output: `[1, 0]`

**Example 3**

- Input: `nums = [8, 4, 7, 0, 0, 6]`
- Output: `[8, 4, 7, 6, 0, 0]`

---

## Solution
### Approach
The problem utilizes a two-pass simulation approach. The first pass performs an in-place modification to handle the doubling logic. The second pass uses a "Two Pointers" technique (specifically a read/write pointer pattern) to partition the array, effectively moving all non-zero elements to the front while preserving their relative order.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We perform two linear passes over the array.
- **Space Complexity**: `O(1)` if we modify the input array in-place, or `O(n)` if we return a new array. The provided solution uses `O(n)` space to return a new array for clarity and safety.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> List[int]:
    n = len(nums)
    # First pass: Apply the doubling operation
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    # Second pass: Shift non-zero elements to the front
    result = [0] * n
    write_idx = 0
    for val in nums:
        if val != 0:
            result[write_idx] = val
            write_idx += 1

    return result
```
</details>
