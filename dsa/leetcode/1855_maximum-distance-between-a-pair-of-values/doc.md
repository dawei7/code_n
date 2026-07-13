# Maximum Distance Between a Pair of Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1855 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-distance-between-a-pair-of-values](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/).

### Goal
Two arrays are nonincreasing. Find the largest distance `j - i` such that `i <= j` and `nums1[i] <= nums2[j]`.

### Function Contract
**Inputs**

- `nums1`: the first nonincreasing integer array.
- `nums2`: the second nonincreasing integer array.

**Return value**

Return the maximum valid distance, or `0` if no positive distance exists.

### Examples
**Example 1**

- Input: `nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]`
- Output: `2`

**Example 2**

- Input: `nums1 = [2,2,2], nums2 = [10,10,1]`
- Output: `1`

**Example 3**

- Input: `nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]`
- Output: `2`

---

## Solution
### Approach
Use two pointers. For each `i` in `nums1`, advance `j` in `nums2` as far right as possible while `j < len(nums2)` and `nums1[i] <= nums2[j]`. Because both arrays are nonincreasing, `j` never needs to move backward. Track `j - i - 1` after the advance.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
