# Sum of Unique Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1748 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-unique-elements](https://leetcode.com/problems/sum-of-unique-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-unique-elements/).

### Goal
Sum the values that appear exactly once in the array.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return the sum of all unique-occurring values.

### Examples
**Example 1**

- Input: `nums = [1,2,3,2]`
- Output: `4`

**Example 2**

- Input: `nums = [1,1,1,1,1]`
- Output: `0`

**Example 3**

- Input: `nums = [1,2,3,4,5]`
- Output: `15`

---

## Solution
### Approach
Count frequencies with a hash map or fixed-size count array. Sum only the values whose final frequency is one.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` or `O(1)` for a bounded value range

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
