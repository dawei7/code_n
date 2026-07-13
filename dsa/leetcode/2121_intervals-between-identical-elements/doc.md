# Intervals Between Identical Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2121 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [intervals-between-identical-elements](https://leetcode.com/problems/intervals-between-identical-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/intervals-between-identical-elements/).

### Goal
For every array position, compute the sum of its index distances to all other positions containing the same value.

### Function Contract
**Inputs**

- `arr`: an integer array.

**Return value**

An array `result` where `result[i]` is the sum of `abs(i - j)` over all `j != i` for which `arr[j] == arr[i]`.

### Examples
**Example 1**

- Input: `arr = [2, 1, 3, 1, 2, 3, 3]`
- Output: `[4, 2, 7, 2, 4, 4, 5]`

**Example 2**

- Input: `arr = [1, 1, 1]`
- Output: `[3, 2, 3]`

**Example 3**

- Input: `arr = [4, 5, 6]`
- Output: `[0, 0, 0]`

---

## Solution
### Approach
Group indices by value. For each sorted index group, use its total index sum and a running prefix sum. At position `i` within a group, distances to earlier indices are `i * index - prefix`, while distances to later indices are `(total - prefix - index) - remaining_count * index`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
