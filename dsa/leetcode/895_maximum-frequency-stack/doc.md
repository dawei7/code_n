# Maximum Frequency Stack

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 895 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Stack, Design, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-frequency-stack](https://leetcode.com/problems/maximum-frequency-stack/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-frequency-stack/).

### Goal
Given two sorted arrays `nums1` and `nums2`, return the median of the two sorted arrays. The overall time complexity must be O(log(m+n)).

### Function Contract
**Inputs**

- `nums1`: List[int] (sorted)
- `nums2`: List[int] (sorted)

**Return value**

float - median of combined arrays

### Examples
**Example 1**

- Input: `nums1 = [1, 3], nums2 = [2]`
- Output: `2.0`

**Example 2**

- Input: `nums1 = [-2], nums2 = [94]`
- Output: `46.0`

**Example 3**

- Input: `nums1 = [-66], nums2 = [45]`
- Output: `-10.5`

---

## Solution
### Approach
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

### Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
