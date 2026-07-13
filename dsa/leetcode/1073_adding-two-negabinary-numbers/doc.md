# Adding Two Negabinary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1073 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [adding-two-negabinary-numbers](https://leetcode.com/problems/adding-two-negabinary-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/adding-two-negabinary-numbers/).

### Goal
Given two arrays of bits that encode non-negative integers in base `-2`, return the bit array for their sum in the same base. The answer must not contain leading zeroes unless the value itself is zero.

### Function Contract
**Inputs**

- `arr1`: most-significant-bit-first representation of a value in base `-2`.
- `arr2`: most-significant-bit-first representation of another value in base `-2`.

**Return value**

A most-significant-bit-first base `-2` representation of the sum.

### Examples
**Example 1**

- Input: `arr1 = [1,1,1,1,1]`, `arr2 = [1,0,1]`
- Output: `[1,0,0,0,0]`

**Example 2**

- Input: `arr1 = [0]`, `arr2 = [0]`
- Output: `[0]`

**Example 3**

- Input: `arr1 = [1]`, `arr2 = [1]`
- Output: `[1,1,0]`

---

## Solution
### Approach
Base conversion, digit-by-digit addition, carry normalization.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(n + m)` for the output digits.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1073: Adding Two Negabinary Numbers."""


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    i = len(arr1) - 1
    j = len(arr2) - 1
    carry = 0
    result: list[int] = []
    while i >= 0 or j >= 0 or carry:
        carry += arr1[i] if i >= 0 else 0
        carry += arr2[j] if j >= 0 else 0
        result.append(carry & 1)
        carry = -(carry >> 1)
        i -= 1
        j -= 1
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result[::-1]
```
</details>
