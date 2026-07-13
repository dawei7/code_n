# Sum of Floored Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1862 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Counting, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-floored-pairs](https://leetcode.com/problems/sum-of-floored-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-floored-pairs/).

### Goal
For every ordered pair `(i, j)`, compute `floor(nums[i] / nums[j])` and sum all values modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

Return the sum of floored pair values modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [2,5,9]`
- Output: `10`

**Example 2**

- Input: `nums = [7,7,7,7,7,7,7]`
- Output: `49`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `7`

---

## Solution
### Approach
Count frequencies of each value and build prefix counts over values. For each possible denominator `d` present in `nums`, group numerators by quotient: values in `[q*d, (q+1)*d - 1]` contribute `q`. Prefix counts give how many numerators fall in each range.

### Complexity Analysis
- **Time Complexity**: `O(M log M)` over value ranges, where `M = max(nums)`
- **Space Complexity**: `O(M)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
