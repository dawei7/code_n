# Number of Good Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1512 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-good-pairs](https://leetcode.com/problems/number-of-good-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-good-pairs/).

### Goal
Count pairs of indices `(i, j)` where `i < j` and `nums[i] == nums[j]`.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The number of good pairs.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1, 1, 3]`
- Output: `4`

**Example 2**

- Input: `nums = [1, 1, 1, 1]`
- Output: `6`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`

---

## Solution
### Approach
Track how many times each value has appeared. When reading a value, every
previous occurrence of the same value forms a new good pair with the current
index, then increment that value's frequency.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(u)`, where `u` is the number of distinct values.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(nums):
    counts = Counter(nums)
    return sum(counts[value] * (counts[value] - 1) // 2 for value in counts)
```
</details>
