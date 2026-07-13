# Form Array by Concatenating Subarrays of Another Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1764 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [form-array-by-concatenating-subarrays-of-another-array](https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/).

### Goal
Check whether every group can be matched as a contiguous subarray of `nums` in order, with no overlap between matched groups.

### Function Contract
**Inputs**

- `groups`: a list of integer arrays to match in order.
- `nums`: the array to search.

**Return value**

Return `True` if all groups can be found consecutively in order, otherwise `False`.

### Examples
**Example 1**

- Input: `groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]`
- Output: `True`

**Example 2**

- Input: `groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]`
- Output: `False`

**Example 3**

- Input: `groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]`
- Output: `False`

---

## Solution
### Approach
Scan `nums` with a pointer. For each group, move the pointer forward until the whole group matches starting there; after a match, advance by the group length so matches cannot overlap. If any group cannot be found, return false.

### Complexity Analysis
- **Time Complexity**: `O(total group length * len(nums))` in the straightforward scan
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
