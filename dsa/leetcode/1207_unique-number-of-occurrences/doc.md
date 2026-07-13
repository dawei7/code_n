# Unique Number of Occurrences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1207 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [unique-number-of-occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/unique-number-of-occurrences/).

### Goal
Determine whether every distinct value in the array appears a unique number of times.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

`true` if no two distinct values have the same frequency, otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [1,2,2,1,1,3]`
- Output: `true`

**Example 2**

- Input: `arr = [1,2]`
- Output: `false`

**Example 3**

- Input: `arr = [-3,0,1,-3,1,1,1,-3,10,0]`
- Output: `true`

---

## Solution
### Approach
Hash-map frequency counting.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(k)` for `k` distinct values.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(arr):
    frequencies = Counter(arr).values()
    return len(set(frequencies)) == len(list(frequencies))
```
</details>
