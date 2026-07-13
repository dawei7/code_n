# Minimum Difference Between Highest and Lowest of K Scores

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1984 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-difference-between-highest-and-lowest-of-k-scores](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/).

### Goal
Choose exactly `k` scores so the difference between the chosen maximum and minimum is as small as possible.

### Function Contract
**Inputs**

- `nums`: student scores.
- `k`: number of scores to choose.

**Return value**

Return the minimum possible difference between highest and lowest selected score.

### Examples
**Example 1**

- Input: `nums = [90], k = 1`
- Output: `0`

**Example 2**

- Input: `nums = [9,4,1,7], k = 2`
- Output: `2`

**Example 3**

- Input: `nums = [1,5,6,14,15], k = 3`
- Output: `5`

---

## Solution
### Approach
Sort the scores. Any optimal set of `k` scores appears as a contiguous window in sorted order, so scan all windows of length `k` and minimize `nums[i + k - 1] - nums[i]`.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` beyond the sort.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
