# Sort Even and Odd Indices Independently

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2164 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sort-even-and-odd-indices-independently](https://leetcode.com/problems/sort-even-and-odd-indices-independently/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sort-even-and-odd-indices-independently/).

### Goal
Rearrange values at even indices into nondecreasing order and values at odd indices into nonincreasing order, without moving a value between index parities.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The array after independently sorting the two parity groups.

### Examples
**Example 1**

- Input: `nums = [4, 1, 2, 3]`
- Output: `[2, 3, 4, 1]`

**Example 2**

- Input: `nums = [2, 1]`
- Output: `[2, 1]`

**Example 3**

- Input: `nums = [5, 8, 3, 6, 1]`
- Output: `[1, 8, 3, 6, 5]`

---

## Solution
### Approach
Extract values from even and odd positions into separate lists. Sort the even list ascending and the odd list descending, then write or interleave them back into their matching positions.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
