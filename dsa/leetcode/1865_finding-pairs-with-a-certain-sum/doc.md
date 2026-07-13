# Finding Pairs With a Certain Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1865 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [finding-pairs-with-a-certain-sum](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/).

### Goal
Design a data structure over two arrays. It must add a value to one element of `nums2`, and count pairs `(i, j)` such that `nums1[i] + nums2[j]` equals a requested total.

### Function Contract
**Inputs**

- Initial arrays `nums1` and `nums2`.
- `add(index, val)`: add `val` to `nums2[index]`.
- `count(tot)`: count pairs summing to `tot`.

**Return value**

Return `null` for construction and updates; return an integer for each count query.

### Examples
**Example 1**

- Input: `["FindSumPairs","count","add","count","count","add","add","count"]`, `[[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8],[4],[0,1],[1,1],[7]]`
- Output: `[null,8,null,2,1,null,null,11]`

**Example 2**

- Input: `["FindSumPairs","count","add","count"]`, `[[[1,2],[3,4]],[5],[0,2],[5]]`
- Output: `[null,2,null,1]`

**Example 3**

- Input: `["FindSumPairs","count"]`, `[[[1],[1]],[2]]`
- Output: `[null,1]`

---

## Solution
### Approach
Keep `nums1` unchanged and maintain a frequency map for current values in `nums2`. On `add`, decrement the old `nums2[index]` count, update the value, and increment the new count. On `count(tot)`, iterate through `nums1` and add the frequency of `tot - value` in `nums2`.

### Complexity Analysis
- **Time Complexity**: `O(1)` for `add`, `O(len(nums1))` for `count`
- **Space Complexity**: `O(len(nums2))`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
