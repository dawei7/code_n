# Kth Missing Positive Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1539 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [kth-missing-positive-number](https://leetcode.com/problems/kth-missing-positive-number/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/kth-missing-positive-number/).

### Goal
Given a strictly increasing positive array, find the `k`th positive integer that
does not appear in the array.

### Function Contract
**Inputs**

- `arr`: a strictly increasing array of positive integers.
- `k`: the 1-based missing-positive rank to find.

**Return value**

The `k`th missing positive integer.

### Examples
**Example 1**

- Input: `arr = [2, 3, 4, 7, 11], k = 5`
- Output: `9`

**Example 2**

- Input: `arr = [1, 2, 3, 4], k = 2`
- Output: `6`

**Example 3**

- Input: `arr = [5, 6, 7], k = 1`
- Output: `1`

---

## Solution
### Approach
For index `i`, the count of missing positives before `arr[i]` is
`arr[i] - i - 1`. Binary-search the first index where that count is at least
`k`, then derive the answer from the previous array value and the remaining
missing count. A linear scan works too, but binary search uses the sorted
property directly.

### Complexity Analysis
- **Time Complexity**: `O(log n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr, k):
    positives = sorted({x for x in arr if x > 0})
    missing = max(1, k)
    current = 1
    for value in positives:
        if value < current:
            continue
        if value == current:
            current += 1
            continue
        gap = value - current
        if missing <= gap:
            return current + missing - 1
        missing -= gap
        current = value + 1
    return current + missing - 1
```
</details>
