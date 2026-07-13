# Detect Pattern of Length M Repeated K or More Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1566 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [detect-pattern-of-length-m-repeated-k-or-more-times](https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/).

### Goal
Determine whether the array contains a contiguous pattern of length `m` repeated
at least `k` times back to back.

### Function Contract
**Inputs**

- `arr`: an integer array.
- `m`: the pattern length.
- `k`: the required consecutive repeat count.

**Return value**

`true` if such a repeated pattern exists; otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [1, 2, 4, 4, 4, 4], m = 1, k = 3`
- Output: `true`

**Example 2**

- Input: `arr = [1, 2, 1, 2, 1, 1, 1, 3], m = 2, k = 2`
- Output: `true`

**Example 3**

- Input: `arr = [1, 2, 1, 2, 1, 3], m = 2, k = 3`
- Output: `false`

---

## Solution
### Approach
Scan possible starting positions. For each start, compare each element with the
corresponding element one pattern length later for `m * (k - 1)` positions. If
all those comparisons match, the repeated block exists.

### Complexity Analysis
- **Time Complexity**: `O(n * m * k)` in the direct check.
- **Space Complexity**: `O(1)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr, m, k):
    if m <= 0 or k <= 0:
        return False
    total = m * k
    for start in range(0, len(arr) - total + 1):
        ok = True
        for offset in range(m, total):
            if arr[start + offset] != arr[start + offset - m]:
                ok = False
                break
        if ok:
            return True
    return False
```
</details>
