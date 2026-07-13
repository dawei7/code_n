# Number of Times Binary String Is Prefix-Aligned

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1375 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-times-binary-string-is-prefix-aligned](https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/).

### Goal
A binary string of length `n` starts with all zeroes. At step `i`, one indexed bit from `flips` becomes `1`. Count how many steps leave every `1` bit inside the prefix `1..i` and every bit after that prefix still `0`.

### Function Contract
**Inputs**

- `flips`: a permutation of positions from `1` to `n` in the order they are turned on.

**Return value**

The number of moments when the turned-on bits exactly form a prefix.

### Examples
**Example 1**

- Input: `flips = [3,2,4,1,5]`
- Output: `2`

**Example 2**

- Input: `flips = [4,1,2,3]`
- Output: `1`

**Example 3**

- Input: `flips = [1,2,3]`
- Output: `3`

---

## Solution
### Approach
Prefix maximum tracking. After `i` flips, the first `i` positions are exactly filled if and only if the maximum flipped position seen so far is `i`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1375: Number of Times Binary String Is Prefix-Aligned."""


def solve(flips: list[int]) -> int:
    answer = 0
    rightmost = 0
    for step, position in enumerate(flips, start=1):
        rightmost = max(rightmost, position)
        if rightmost == step:
            answer += 1
    return answer
```
</details>
