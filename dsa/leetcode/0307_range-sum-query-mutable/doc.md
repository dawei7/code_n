# Range Sum Query - Mutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 307 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Design, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problem Description
### Goal
Construct a mutable range-sum structure from an initial integer array. Operations arrive sequentially: `update(index, value)` replaces the current value at one valid position, while `sumRange(left, right)` asks about the current array after all preceding updates.

For every sum query, return the total from `left` through `right`, including both endpoints. Updates produce no output and are assignments rather than increments. Support interleaved operations efficiently, avoiding a full-array rebuild or full-range scan per call. The app contract executes the active operation prefix and returns sum results in order; the native `NumArray` retains state across methods.

### Function Contract
**Inputs**

- `arr`: the initial integer array
- `n`: the active prefix length of `arr`
- `queries`: ordered operations `["update", index, value]` or `["sum", left, right]`
- `q`: the number of operations from `queries` to execute

**Return value**

The results of all executed `sum` operations, in operation order. Updates produce no output.

### Examples
**Example 1**

- Input: `arr = [1,3,5], n = 3, queries = [["sum",0,2],["update",1,2],["sum",0,2]], q = 3`
- Output: `[9,8]`

**Example 2**

- Input: `arr = [4], n = 1, queries = [["sum",0,0],["update",0,7],["sum",0,0]], q = 3`
- Output: `[4,7]`

**Example 3**

- Input: `arr = [2,4,6,8], n = 4, queries = [["sum",1,3],["update",2,1],["sum",0,2]], q = 3`
- Output: `[18,7]`
