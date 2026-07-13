# Minimum Operations to Make a Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1713 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-a-subsequence](https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/).

### Goal
Insert numbers anywhere in `arr` until `target` becomes a subsequence. Values in `target` are distinct. Find the minimum insertions needed.

### Function Contract
**Inputs**

- `target`: a list of distinct integers.
- `arr`: a list of integers.

**Return value**

Return the fewest insertions required to make `target` appear as a subsequence of `arr`.

### Examples
**Example 1**

- Input: `target = [5,1,3], arr = [9,4,2,3,4]`
- Output: `2`

**Example 2**

- Input: `target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]`
- Output: `3`

**Example 3**

- Input: `target = [1,2,3], arr = [1,2,3]`
- Output: `0`

---

## Solution
### Approach
Map each target value to its index, then translate `arr` into target indices while skipping values not in `target`. The longest increasing subsequence of that index sequence is the longest part of `target` already present in order. Insert every missing target value, so the answer is `len(target) - LIS_length`.

### Complexity Analysis
- **Time Complexity**: `O((n + m) log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
