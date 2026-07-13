# Divide Array in Sets of K Consecutive Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1296 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [divide-array-in-sets-of-k-consecutive-numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/).

### Goal
Decide whether the array can be partitioned into groups of size `k`, where each group consists of consecutive integer values.

### Function Contract
**Inputs**

- `nums`: integer array.
- `k`: required group length.

**Return value**

`true` if such a partition exists, otherwise `false`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,3,4,4,5,6]`, `k = 4`
- Output: `true`

**Example 2**

- Input: `nums = [3,3,2,2,1,1]`, `k = 3`
- Output: `true`

**Example 3**

- Input: `nums = [1,2,3,4]`, `k = 3`
- Output: `false`

---

## Solution
### Approach
Greedy counting over sorted values.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(nums, k):
    counts = Counter(nums)
    for start in sorted(counts):
        amount = counts[start]
        if amount == 0:
            continue
        for value in range(start, start + k):
            if counts[value] < amount:
                return False
            counts[value] -= amount
    return True
```
</details>
