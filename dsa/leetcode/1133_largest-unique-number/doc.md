# Largest Unique Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1133 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [largest-unique-number](https://leetcode.com/problems/largest-unique-number/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/largest-unique-number/).

### Goal
Return the largest integer in the array that appears exactly once. If every value appears more than once, return `-1`.

### Function Contract
**Inputs**

- `nums`: List of integers.

**Return value**

Largest unique value, or `-1`.

### Examples
**Example 1**

- Input: `nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]`
- Output: `8`

**Example 2**

- Input: `nums = [9, 9, 8, 8]`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 2, 3, 2, 1]`
- Output: `3`

---

## Solution
### Approach
Count the frequency of each number with a hash map. Then scan the counted values and keep the largest number whose frequency is `1`.

Sorting descending is another option, but counting keeps the logic direct.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)` for the frequency map.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
