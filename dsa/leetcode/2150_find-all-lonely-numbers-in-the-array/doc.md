# Find All Lonely Numbers in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2150 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-all-lonely-numbers-in-the-array](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/).

### Goal
A number is lonely when it appears exactly once and neither adjacent integer, one less or one greater, appears in the array. Return all lonely values in any order.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

A list of all lonely numbers, in any order.

### Examples
**Example 1**

- Input: `nums = [10, 6, 5, 8]`
- Output: `[10, 8]`

**Example 2**

- Input: `nums = [1, 3, 5, 3]`
- Output: `[1, 5]`

**Example 3**

- Input: `nums = [2, 2, 3, 4]`
- Output: `[]`

---

## Solution
### Approach
Build a frequency map. A distinct key `x` belongs in the result exactly when its frequency is one and neither `x - 1` nor `x + 1` is a key in the map.

### Complexity Analysis
- **Time Complexity**: `O(n)` expected
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
