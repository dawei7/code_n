# Keep Multiplying Found Values by Two

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2154 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [keep-multiplying-found-values-by-two](https://leetcode.com/problems/keep-multiplying-found-values-by-two/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/keep-multiplying-found-values-by-two/).

### Goal
Starting from `original`, repeatedly double the current value while that value occurs in the array. Return the first value not found.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `original`: the initial positive integer.

**Return value**

The value reached after all required doublings.

### Examples
**Example 1**

- Input: `nums = [5, 3, 6, 1, 12]`, `original = 3`
- Output: `24`

**Example 2**

- Input: `nums = [2, 7, 9]`, `original = 4`
- Output: `4`

**Example 3**

- Input: `nums = [1, 2, 4, 8]`, `original = 1`
- Output: `16`

---

## Solution
### Approach
Put all array values in a hash set. While the current value is present, multiply it by two. Membership checks do not consume occurrences because only presence matters.

### Complexity Analysis
- **Time Complexity**: `O(n)` expected
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
