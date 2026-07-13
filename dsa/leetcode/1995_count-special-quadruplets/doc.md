# Count Special Quadruplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1995 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-special-quadruplets](https://leetcode.com/problems/count-special-quadruplets/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-special-quadruplets/).

### Goal
Count quadruplets of indices `a < b < c < d` such that `nums[a] + nums[b] + nums[c] == nums[d]`.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the number of special quadruplets.

### Examples
**Example 1**

- Input: `nums = [1,2,3,6]`
- Output: `1`

**Example 2**

- Input: `nums = [3,3,6,4,5]`
- Output: `0`

**Example 3**

- Input: `nums = [1,1,1,3,5]`
- Output: `4`

---

## Solution
### Approach
For a direct solution, enumerate the first three indices and check the fourth value. A faster version scans middle indices while counting future differences `nums[d] - nums[c]`, then matches them with earlier pair sums.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` with pair-sum/difference counting.
- **Space Complexity**: `O(V)` for counted sums/differences.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
