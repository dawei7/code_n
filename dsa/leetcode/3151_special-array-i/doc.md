# Special Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3151 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [special-array-i](https://leetcode.com/problems/special-array-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/special-array-i/).

### Goal
Determine if a given array of integers is "special." An array is defined as special if every pair of adjacent elements has different parity (i.e., one is even and the other is odd). If the array contains only one element, it is considered special by default.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- `bool`: Returns `True` if all adjacent elements have different parity, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1]`
- Output: `True`

**Example 2**

- Input: `nums = [2, 1, 4]`
- Output: `True`

**Example 3**

- Input: `nums = [4, 3, 1, 6]`
- Output: `False`

---

## Solution
### Approach
Linear scan (Iteration). The algorithm iterates through the array once, comparing the parity of each element with its immediate successor using the modulo operator (`% 2`).

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the list.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space for iteration variables.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> bool:
    """
    Determines if an array is 'special' by checking if all adjacent
    elements have different parity.
    """
    if len(nums) <= 1:
        return True

    for i in range(len(nums) - 1):
        # Check if both numbers have the same parity
        # If (a % 2) == (b % 2), they are both even or both odd
        if nums[i] % 2 == nums[i + 1] % 2:
            return False

    return True
```
</details>
