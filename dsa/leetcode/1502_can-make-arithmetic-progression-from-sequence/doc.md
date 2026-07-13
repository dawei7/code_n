# Can Make Arithmetic Progression From Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1502 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [can-make-arithmetic-progression-from-sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/).

### Goal
Determine whether the array can be reordered into an arithmetic progression.

### Function Contract
**Inputs**

- `arr`: an integer array.

**Return value**

`true` if some ordering has a constant adjacent difference; otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [3, 5, 1]`
- Output: `true`

**Example 2**

- Input: `arr = [1, 2, 4]`
- Output: `false`

**Example 3**

- Input: `arr = [7, 7, 7]`
- Output: `true`

---

## Solution
### Approach
Sort the values, compute the first adjacent difference, and verify every later
adjacent pair has the same difference.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(1)` extra space if sorting in place.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr):
    if len(arr) <= 2:
        return True
    ordered = sorted(arr)
    diff = ordered[1] - ordered[0]
    return all(ordered[i] - ordered[i - 1] == diff for i in range(2, len(ordered)))
```
</details>
