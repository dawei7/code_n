# Range Sum Query - Immutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 303 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Design, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-query-immutable/) |

## Problem Description
### Goal
Construct a `NumArray` from a nonempty integer array that will not change after construction. The object receives repeated `sumRange(left, right)` queries using valid zero-based endpoints with `left <= right`.

For each query, return the sum of all array values from index `left` through index `right`, including both endpoints. Negative values and repeated queries must be handled normally. Perform preprocessing once so each later query is answered in constant time rather than resumming its interval. The app adapter returns all query results in order, while the native class preserves the immutable array state between method calls.

### Function Contract
**Inputs**

- `nums`: a nonempty immutable list of integers
- `queries`: a list of pairs `[left, right]` with valid inclusive indices

**Return value**

A list containing `nums[left] + ... + nums[right]` for each query in the original query order.

### Examples
**Example 1**

- Input: `nums = [-2,0,3,-5,2,-1], queries = [[0,2],[2,5],[0,5]]`
- Output: `[1,-1,-3]`

**Example 2**

- Input: `nums = [1,2], queries = [[0,0],[1,1]]`
- Output: `[1,2]`

**Example 3**

- Input: `nums = [5], queries = [[0,0]]`
- Output: `[5]`
