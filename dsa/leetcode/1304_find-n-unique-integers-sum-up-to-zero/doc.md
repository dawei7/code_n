# Find N Unique Integers Sum up to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1304 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-n-unique-integers-sum-up-to-zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/).

### Goal
Return any `n` distinct integers whose sum is zero.

### Function Contract
**Inputs**

- `n`: number of integers to return.

**Return value**

A list of `n` unique integers with total sum `0`.

### Examples
**Example 1**

- Input: `n = 5`
- Output: `[-2,-1,0,1,2]`

**Example 2**

- Input: `n = 3`
- Output: `[-1,0,1]`

**Example 3**

- Input: `n = 4`
- Output: `[-2,-1,1,2]`

---

## Solution
### Approach
Symmetric pair construction.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the output.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n):
    result = []
    for value in range(1, n // 2 + 1):
        result.extend([value, -value])
    if n % 2:
        result.append(0)
    return result
```
</details>
