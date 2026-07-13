# Sum of Absolute Differences in a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1685 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-absolute-differences-in-a-sorted-array](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/).

### Goal
For each element in a sorted integer array, compute the sum of absolute differences between that element and every other element.

### Function Contract
**Inputs**

- `nums`: a nondecreasing integer array.

**Return value**

Return an array where position `i` contains `sum(abs(nums[i] - nums[j]))` for all `j`.

### Examples
**Example 1**

- Input: `nums = [2,3,5]`
- Output: `[4,3,5]`

**Example 2**

- Input: `nums = [1,4,6,8,10]`
- Output: `[24,15,13,15,21]`

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `[0,0,0]`

---

## Solution
### Approach
Use prefix sums. For index `i`, all values on the left are at most `nums[i]`, contributing `nums[i] * i - prefix_left`. Values on the right contribute `suffix_right - nums[i] * right_count`. Add the two contributions for each index.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` besides the output array

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
