# Maximum of Absolute Value Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1131 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-of-absolute-value-expression](https://leetcode.com/problems/maximum-of-absolute-value-expression/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-of-absolute-value-expression/).

### Goal
For arrays `arr1` and `arr2`, maximize `|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|` over all valid indices.

### Function Contract
**Inputs**

- `arr1`: first integer array.
- `arr2`: second integer array of the same length.

**Return value**

The maximum expression value.

### Examples
**Example 1**

- Input: `arr1 = [1,2,3,4]`, `arr2 = [-1,4,5,6]`
- Output: `13`

**Example 2**

- Input: `arr1 = [1,-2,-5,0,10]`, `arr2 = [0,-2,-1,-7,-4]`
- Output: `20`

**Example 3**

- Input: `arr1 = [0,0]`, `arr2 = [0,1]`
- Output: `2`

---

## Solution
### Approach
Sign expansion of absolute values.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr1, arr2):
    best = 0
    for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        low = float("inf")
        high = float("-inf")
        for i, (a, b) in enumerate(zip(arr1, arr2)):
            value = s1 * a + s2 * b + i
            low = min(low, value)
            high = max(high, value)
        best = max(best, high - low)
    return best
```
</details>
