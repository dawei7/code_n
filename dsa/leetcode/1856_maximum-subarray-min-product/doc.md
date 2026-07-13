# Maximum Subarray Min-Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1856 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-subarray-min-product](https://leetcode.com/problems/maximum-subarray-min-product/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-subarray-min-product/).

### Goal
For every non-empty subarray, its min-product is the subarray minimum multiplied by the subarray sum. Find the maximum min-product and return it modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

Return the maximum subarray min-product modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,2]`
- Output: `14`

**Example 2**

- Input: `nums = [2,3,3,1,2]`
- Output: `18`

**Example 3**

- Input: `nums = [3,1,5,6,4,2]`
- Output: `60`

---

## Solution
### Approach
Use prefix sums for subarray sums and a monotonic increasing stack to find, for each index, the largest interval where `nums[i]` is the minimum. The best min-product using that element as the minimum is `nums[i] * sum(interval)`. Take the maximum over all indices.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
