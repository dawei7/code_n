# Number of Different Subsequences GCDs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1819 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Counting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-different-subsequences-gcds](https://leetcode.com/problems/number-of-different-subsequences-gcds/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-different-subsequences-gcds/).

### Goal
Count how many distinct positive integers can appear as the greatest common divisor of some non-empty subsequence of `nums`.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

Return the number of distinct subsequence GCD values.

### Examples
**Example 1**

- Input: `nums = [6,10,3]`
- Output: `5`

**Example 2**

- Input: `nums = [5,15,40,5,6]`
- Output: `7`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `3`

---

## Solution
### Approach
Mark which values are present. For every candidate gcd `g`, scan multiples of `g` that appear in `nums` and maintain their running gcd. If the running gcd becomes `g`, then some subsequence has gcd `g`, so count it and stop scanning that candidate.

### Complexity Analysis
- **Time Complexity**: `O(M log M)` style multiple scanning, where `M = max(nums)`
- **Space Complexity**: `O(M)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
