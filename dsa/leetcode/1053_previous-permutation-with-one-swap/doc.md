# Previous Permutation With One Swap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1053 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [previous-permutation-with-one-swap](https://leetcode.com/problems/previous-permutation-with-one-swap/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/previous-permutation-with-one-swap/).

### Goal
Given an array of positive integers, make at most one swap to produce the lexicographically largest array that is still strictly smaller than the original.

### Function Contract
**Inputs**

- `arr`: List[int]

**Return value**

List[int] - previous permutation after at most one swap

### Examples
**Example 1**

- Input: `arr = [3, 2, 1]`
- Output: `[3, 1, 2]`

**Example 2**

- Input: `arr = [1, 1, 5]`
- Output: `[1, 1, 5]`

**Example 3**

- Input: `arr = [1, 9, 4, 6, 7]`
- Output: `[1, 7, 4, 6, 9]`

---

## Solution
### Approach
Greedy previous-permutation pivot selection.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1053: Previous Permutation With One Swap."""


def solve(arr: list[int]) -> list[int]:
    i = len(arr) - 2
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1
    if i < 0:
        return arr

    j = len(arr) - 1
    while arr[j] >= arr[i]:
        j -= 1
    while j > i and arr[j] == arr[j - 1]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    return arr
```
</details>
