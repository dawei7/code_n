# Intersection of Multiple Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2248 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [intersection-of-multiple-arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/intersection-of-multiple-arrays/).

### Goal
Return the values present in every one of several arrays, sorted increasingly. Values within each individual array are distinct.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integer arrays.

**Return value**

The sorted intersection shared by all arrays.

### Examples
**Example 1**

- Input: `nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]`
- Output: `[3, 4]`

**Example 2**

- Input: `nums = [[1, 2, 3], [4, 5, 6]]`
- Output: `[]`

**Example 3**

- Input: `nums = [[7, 2]]`
- Output: `[2, 7]`

---

## Solution
### Approach
Count in how many arrays each value occurs. Because each inner array contains no duplicates, a value belongs to the intersection exactly when its count equals the number of arrays. Collect those values and sort them.

### Complexity Analysis
- **Time Complexity**: `O(E + r log r)`, where `E` is the total number of elements and `r` is the result size
- **Space Complexity**: `O(u)`, where `u` is the number of distinct values

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
