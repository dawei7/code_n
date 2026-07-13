# Reduce Array Size to The Half

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1338 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reduce-array-size-to-the-half](https://leetcode.com/problems/reduce-array-size-to-the-half/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reduce-array-size-to-the-half/).

### Goal
Remove all occurrences of as few distinct integers as possible so that the remaining array length is at most half of the original length.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

The minimum number of distinct values to remove.

### Examples
**Example 1**

- Input: `arr = [3,3,3,3,5,5,5,2,2,7]`
- Output: `2`

**Example 2**

- Input: `arr = [7,7,7,7,7,7]`
- Output: `1`

**Example 3**

- Input: `arr = [1,2,3,4]`
- Output: `2`

---

## Solution
### Approach
Frequency counting and greedy selection.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(arr):
    removed = 0
    answer = 0
    target = len(arr) // 2
    for count in sorted(Counter(arr).values(), reverse=True):
        removed += count
        answer += 1
        if removed >= target:
            return answer
    return answer
```
</details>
