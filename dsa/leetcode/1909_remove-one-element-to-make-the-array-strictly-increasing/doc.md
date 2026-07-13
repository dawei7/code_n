# Remove One Element to Make the Array Strictly Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1909 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [remove-one-element-to-make-the-array-strictly-increasing](https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/).

### Goal
Determine whether removing exactly one element, or effectively choosing one element to skip, can make the array strictly increasing.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return `True` if the array can be made strictly increasing by removing one element, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1,2,10,5,7]`
- Output: `True`

**Example 2**

- Input: `nums = [2,3,1,2]`
- Output: `False`

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `False`

---

## Solution
### Approach
Scan for places where `nums[i] <= nums[i - 1]`. More than one violation cannot be fixed by one removal. At a single violation, it is valid if removing the left element or the right element preserves strict order with the surrounding values.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
