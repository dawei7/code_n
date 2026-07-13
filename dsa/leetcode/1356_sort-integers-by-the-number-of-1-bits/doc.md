# Sort Integers by The Number of 1 Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1356 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sort-integers-by-the-number-of-1-bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/).

### Goal
Sort integers first by how many `1` bits appear in their binary representation, and use the numeric value as the tiebreaker.

### Function Contract
**Inputs**

- `arr`: a list of non-negative integers.

**Return value**

A sorted list following bit-count order and then ascending numeric order.

### Examples
**Example 1**

- Input: `arr = [0,1,2,3,4,5,6,7,8]`
- Output: `[0,1,2,4,8,3,5,6,7]`

**Example 2**

- Input: `arr = [5,3,7,10]`
- Output: `[3,5,10,7]`

**Example 3**

- Input: `arr = [2,2,1]`
- Output: `[1,2,2]`

---

## Solution
### Approach
Custom-key sorting. Compute each number's population count and sort by the tuple `(bit_count, value)`.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` comparisons, with constant-time bit counts for bounded machine integers.
- **Space Complexity**: `O(n)` for the sorted output or sorting buffer.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1356: Sort Integers by The Number of 1 Bits."""


def solve(arr: list[int]) -> list[int]:
    return sorted(arr, key=lambda value: (value.bit_count(), value))
```
</details>
