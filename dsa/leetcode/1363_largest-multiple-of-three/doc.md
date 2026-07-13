# Largest Multiple of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1363 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [largest-multiple-of-three](https://leetcode.com/problems/largest-multiple-of-three/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/largest-multiple-of-three/).

### Goal
Given digits, choose some or all of them and arrange the chosen digits to form the largest possible integer that is divisible by `3`. Return the number as a string, or an empty string if no such positive-length number exists.

### Function Contract
**Inputs**

- `digits`: a list of digits from `0` to `9`.

**Return value**

The largest divisible-by-three number that can be formed, with no leading zeroes unless the answer is exactly `"0"`.

### Examples
**Example 1**

- Input: `digits = [8,1,9]`
- Output: `"981"`

**Example 2**

- Input: `digits = [8,6,7,1,0]`
- Output: `"8760"`

**Example 3**

- Input: `digits = [1]`
- Output: `""`

---

## Solution
### Approach
Digit counting and divisibility by remainder. Count digits, compute the total modulo `3`, remove the smallest possible digit set that fixes the remainder, then emit remaining digits from `9` down to `0`.

### Complexity Analysis
- **Time Complexity**: `O(n + 10)`
- **Space Complexity**: `O(10)` besides the output string.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1363: Largest Multiple of Three."""


def solve(digits: list[int]) -> str:
    counts = [0] * 10
    total = 0
    for digit in digits:
        counts[digit] += 1
        total += digit

    def remove_one(remainder: int) -> bool:
        for digit in range(remainder, 10, 3):
            if counts[digit]:
                counts[digit] -= 1
                return True
        return False

    def remove_two(remainder: int) -> bool:
        removed: list[int] = []
        for digit in range(remainder, 10, 3):
            while counts[digit] and len(removed) < 2:
                counts[digit] -= 1
                removed.append(digit)
            if len(removed) == 2:
                return True
        for digit in removed:
            counts[digit] += 1
        return False

    remainder = total % 3
    if remainder == 1:
        if not remove_one(1):
            remove_two(2)
    elif remainder == 2:
        if not remove_one(2):
            remove_two(1)

    answer = "".join(str(digit) * counts[digit] for digit in range(9, -1, -1))
    if not answer:
        return ""
    return "0" if answer[0] == "0" else answer
```
</details>
