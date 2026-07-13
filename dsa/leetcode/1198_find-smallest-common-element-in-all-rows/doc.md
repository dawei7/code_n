# Find Smallest Common Element in All Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1198 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Matrix, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-smallest-common-element-in-all-rows](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/).

### Goal
Given a matrix whose rows are sorted in increasing order, return the smallest element that appears in every row. Return `-1` if no such element exists.

### Function Contract
**Inputs**

- `mat`: Row-sorted integer matrix.

**Return value**

Smallest common element, or `-1`.

### Examples
**Example 1**

- Input: `mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]`
- Output: `5`

**Example 2**

- Input: `mat = [[1,2,3],[4,5,6]]`
- Output: `-1`

**Example 3**

- Input: `mat = [[1,2],[1,3]]`
- Output: `1`

---

## Solution
### Approach
Because each row is sorted, several approaches work. A simple robust method counts each value once per row and returns the first value whose count reaches the number of rows.

Another option is to use one pointer per row and repeatedly advance rows with smaller current values until all rows match.

### Complexity Analysis
- **Time Complexity**: `O(rows * cols)`.
- **Space Complexity**: `O(values)` for counting, or `O(rows)` with the pointer method.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
