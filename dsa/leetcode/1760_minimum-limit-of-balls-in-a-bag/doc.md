# Minimum Limit of Balls in a Bag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1760 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-limit-of-balls-in-a-bag](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/).

### Goal
You may split a bag of balls into two bags, and each split counts as one operation. After at most `maxOperations`, minimize the largest number of balls in any bag.

### Function Contract
**Inputs**

- `nums`: ball counts in the initial bags.
- `maxOperations`: the maximum number of splits allowed.

**Return value**

Return the minimum possible maximum bag size.

### Examples
**Example 1**

- Input: `nums = [9], maxOperations = 2`
- Output: `3`

**Example 2**

- Input: `nums = [2,4,8,2], maxOperations = 4`
- Output: `2`

**Example 3**

- Input: `nums = [7,17], maxOperations = 2`
- Output: `7`

---

## Solution
### Approach
Binary search the answer. For a proposed maximum size `x`, a bag with `v` balls needs `(v - 1) // x` splits to make every resulting bag have at most `x` balls. The candidate is feasible if the total splits is within `maxOperations`.

### Complexity Analysis
- **Time Complexity**: `O(n log max(nums))`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
