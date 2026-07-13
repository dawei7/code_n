# Four Divisors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1390 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [four-divisors](https://leetcode.com/problems/four-divisors/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/four-divisors/).

### Goal
For each input number, determine whether it has exactly four positive divisors. If it does, add the sum of those divisors to the answer.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

The total sum of divisors across numbers that have exactly four divisors.

### Examples
**Example 1**

- Input: `nums = [21,4,7]`
- Output: `32`

**Example 2**

- Input: `nums = [10,12]`
- Output: `18`

**Example 3**

- Input: `nums = [16,25]`
- Output: `0`

---

## Solution
### Approach
Divisor enumeration up to the square root. Track found divisor pairs and stop early once more than four divisors are discovered.

### Complexity Analysis
- **Time Complexity**: `O(n * sqrt(M))`, where `M` is the largest number.
- **Space Complexity**: `O(1)` besides a small divisor counter/sum.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1390: Four Divisors."""

from math import isqrt


def solve(nums: list[int]) -> int:
    total = 0
    for value in nums:
        divisor_count = 0
        divisor_sum = 0
        for d in range(1, isqrt(value) + 1):
            if value % d != 0:
                continue
            other = value // d
            if other == d:
                divisor_count += 1
                divisor_sum += d
            else:
                divisor_count += 2
                divisor_sum += d + other
            if divisor_count > 4:
                break
        if divisor_count == 4:
            total += divisor_sum
    return total
```
</details>
