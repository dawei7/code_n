# Maximum Score Of Spliced Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2321 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-score-of-spliced-array](https://leetcode.com/problems/maximum-score-of-spliced-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-score-of-spliced-array/).

### Goal
Optionally choose one nonempty interval and swap that interval between two equal-length arrays. Maximize the sum of either resulting array.

### Function Contract
**Inputs**

- `nums1`, `nums2`: equal-length integer arrays.

**Return value**

The largest sum achievable for either array after at most one interval swap.

### Examples
**Example 1**

- Input: `nums1 = [60, 60, 60]`, `nums2 = [10, 90, 10]`
- Output: `210`

**Example 2**

- Input: `nums1 = [20, 40, 20, 70, 30]`, `nums2 = [50, 20, 50, 40, 20]`
- Output: `220`

**Example 3**

- Input: `nums1 = [1]`, `nums2 = [2]`
- Output: `2`

---

## Solution
### Approach
For improving `nums1`, swapping index `i` changes its sum by `nums2[i] - nums1[i]`; the best interval gain is the maximum subarray sum of that difference array. Compute the analogous gain for `nums2` using the negated differences. Return the larger original sum plus its nonnegative best gain.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
