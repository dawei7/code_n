# Binary Prefix Divisible By 5

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1018 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [binary-prefix-divisible-by-5](https://leetcode.com/problems/binary-prefix-divisible-by-5/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/binary-prefix-divisible-by-5/).

### Goal
For each prefix of a binary array, interpret that prefix as a binary number and report whether it is divisible by `5`.

### Function Contract
**Inputs**

- `nums`: List[int] containing only `0` and `1`

**Return value**

List[bool] - divisibility result for each prefix

### Examples
**Example 1**

- Input: `nums = [0, 1, 1]`
- Output: `[True, False, False]`

**Example 2**

- Input: `nums = [1, 1, 1]`
- Output: `[False, False, False]`

**Example 3**

- Input: `nums = [1, 0, 1, 0]`
- Output: `[False, False, True, True]`

---

## Solution
### Approach
Rolling modulo arithmetic over binary prefixes.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` auxiliary space excluding the output

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1018: Binary Prefix Divisible By 5."""


def solve(nums: list[int]) -> list[bool]:
    value = 0
    answer: list[bool] = []
    for bit in nums:
        value = ((value << 1) + bit) % 5
        answer.append(value == 0)
    return answer
```
</details>
