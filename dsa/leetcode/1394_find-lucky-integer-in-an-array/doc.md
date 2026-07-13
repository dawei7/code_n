# Find Lucky Integer in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1394 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-lucky-integer-in-an-array](https://leetcode.com/problems/find-lucky-integer-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-lucky-integer-in-an-array/).

### Goal
A lucky integer is a value whose frequency in the array equals the value itself. Return the largest lucky integer, or `-1` if none exists.

### Function Contract
**Inputs**

- `arr`: a list of integers.

**Return value**

The largest lucky integer in `arr`, or `-1`.

### Examples
**Example 1**

- Input: `arr = [2,2,3,4]`
- Output: `2`

**Example 2**

- Input: `arr = [1,2,2,3,3,3]`
- Output: `3`

**Example 3**

- Input: `arr = [5]`
- Output: `-1`

---

## Solution
### Approach
Frequency counting. Count occurrences of each value, then scan the keys for values whose count equals the value and keep the maximum.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(u)` where `u` is the number of distinct values.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1394: Find Lucky Integer in an Array."""

from collections import Counter


def solve(arr: list[int]) -> int:
    counts = Counter(arr)
    return max((value for value, count in counts.items() if value == count), default=-1)
```
</details>
