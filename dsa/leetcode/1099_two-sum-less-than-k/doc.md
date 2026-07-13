# Two Sum Less Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1099 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [two-sum-less-than-k](https://leetcode.com/problems/two-sum-less-than-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/two-sum-less-than-k/).

### Goal
Find the largest possible sum of two distinct array elements that is strictly less than `k`. Return `-1` if no such pair exists.

### Function Contract
**Inputs**

- `nums`: List of integers.
- `k`: Strict upper bound for the pair sum.

**Return value**

Maximum valid pair sum, or `-1`.

### Examples
**Example 1**

- Input: `nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60`
- Output: `58`

**Example 2**

- Input: `nums = [10, 20, 30], k = 15`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 2, 3, 4], k = 6`
- Output: `5`

---

## Solution
### Approach
Sort the array and use two pointers. If `nums[left] + nums[right]` is less than `k`, it is a candidate answer, and increasing `left` may produce a larger sum. If the sum is at least `k`, decrease `right` to make the sum smaller.

The best candidate seen during the scan is the answer.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` for sorting.
- **Space Complexity**: `O(1)` extra space if sorting in place, aside from language-specific sort overhead.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
