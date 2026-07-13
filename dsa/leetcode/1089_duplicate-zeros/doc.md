# Duplicate Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1089 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [duplicate-zeros](https://leetcode.com/problems/duplicate-zeros/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/duplicate-zeros/).

### Goal
Modify the array in place as if every zero were duplicated and the array were then truncated back to its original length.

### Function Contract
**Inputs**

- `arr`: a mutable integer array.

**Return value**

No value is returned; `arr` is changed in place.

### Examples
**Example 1**

- Input: `arr = [1,0,2,3,0,4,5,0]`
- Output: `[1,0,0,2,3,0,0,4]`

**Example 2**

- Input: `arr = [1,2,3]`
- Output: `[1,2,3]`

**Example 3**

- Input: `arr = [0,0,1]`
- Output: `[0,0,0]`

---

## Solution
### Approach
Two pointers, in-place backward writing.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` extra space.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1089: Duplicate Zeros."""


def solve(arr: list[int]) -> list[int]:
    n = len(arr)
    possible_dups = 0
    last = n - 1
    left = 0
    while left <= last - possible_dups:
        if arr[left] == 0:
            if left == last - possible_dups:
                arr[last] = 0
                last -= 1
                break
            possible_dups += 1
        left += 1

    for i in range(last - possible_dups, -1, -1):
        if arr[i] == 0:
            arr[i + possible_dups] = 0
            possible_dups -= 1
            arr[i + possible_dups] = 0
        else:
            arr[i + possible_dups] = arr[i]
    return arr
```
</details>
