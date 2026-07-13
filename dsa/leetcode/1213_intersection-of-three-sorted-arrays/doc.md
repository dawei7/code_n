# Intersection of Three Sorted Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1213 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [intersection-of-three-sorted-arrays](https://leetcode.com/problems/intersection-of-three-sorted-arrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/intersection-of-three-sorted-arrays/).

### Goal
Return every integer that appears in all three input arrays. The arrays are strictly increasing, so the answer is also increasing.

### Function Contract
**Inputs**

- `arr1: List[int]` - First strictly increasing integer array.
- `arr2: List[int]` - Second strictly increasing integer array.
- `arr3: List[int]` - Third strictly increasing integer array.

**Return value**

`List[int]` - Values present in all three arrays.

### Examples
**Example 1**

- Input: `arr1 = [1, 2, 3, 4, 5], arr2 = [1, 2, 5, 7, 9], arr3 = [1, 3, 4, 5, 8]`
- Output: `[1, 5]`

**Example 2**

- Input: `arr1 = [197, 418, 523, 876, 1356], arr2 = [501, 880, 1593, 1710, 1870], arr3 = [521, 682, 1337, 1395, 1764]`
- Output: `[]`

**Example 3**

- Input: `arr1 = [2, 4, 6], arr2 = [1, 2, 3, 4, 5, 6], arr3 = [2, 6, 8]`
- Output: `[2, 6]`

---

## Solution
### Approach
Use three pointers, one per array. When all pointed values are equal, append that value and advance all pointers. Otherwise advance every pointer currently pointing at the smallest value, because that value cannot appear later in the other sorted arrays.

### Complexity Analysis
- **Time Complexity**: `O(n1 + n2 + n3)`, where `n1`, `n2`, and `n3` are the array lengths.
- **Space Complexity**: `O(1)` auxiliary space, excluding the returned list.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
