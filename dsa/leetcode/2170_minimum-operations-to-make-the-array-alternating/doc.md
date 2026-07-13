# Minimum Operations to Make the Array Alternating

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2170 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-the-array-alternating](https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/).

### Goal
Change as few array elements as possible so all even indices hold one common value, all odd indices hold another common value, and those two values differ.

### Function Contract
**Inputs**

- `nums`: an integer array; one operation replaces any element with any positive integer.

**Return value**

The minimum number of replacement operations needed to make the array alternating.

### Examples
**Example 1**

- Input: `nums = [3, 1, 3, 2, 4, 3]`
- Output: `3`

**Example 2**

- Input: `nums = [1, 2, 2, 2, 2]`
- Output: `2`

**Example 3**

- Input: `nums = [1]`
- Output: `0`

---

## Solution
### Approach
Count frequencies separately at even and odd indices. Only the two most frequent candidates from each side can matter. Try the constant number of pairs among those candidates whose values differ, maximize the elements left unchanged, and subtract that maximum from `n`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` in the worst case for frequency maps

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
