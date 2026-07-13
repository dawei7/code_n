# Count Number of Maximum Bitwise-OR Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2044 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-number-of-maximum-bitwise-or-subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/).

### Goal
Among all non-empty subsets, count how many have the maximum possible bitwise OR value.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the number of subsets whose OR equals the OR of all elements.

### Examples
**Example 1**

- Input: `nums = [3,1]`
- Output: `2`

**Example 2**

- Input: `nums = [2,2,2]`
- Output: `7`

**Example 3**

- Input: `nums = [3,2,1,5]`
- Output: `6`

---

## Solution
### Approach
First compute the target OR of the entire array. Then backtrack over include/exclude choices, or use DP counts by OR value, and count subsets that reach the target.

### Complexity Analysis
- **Time Complexity**: `O(2^n)` with backtracking.
- **Space Complexity**: `O(n)` recursion stack.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
