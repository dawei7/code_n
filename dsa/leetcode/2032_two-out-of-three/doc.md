# Two Out of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2032 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [two-out-of-three](https://leetcode.com/problems/two-out-of-three/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/two-out-of-three/).

### Goal
Find values that appear in at least two of the three given arrays.

### Function Contract
**Inputs**

- `nums1`, `nums2`, `nums3`: integer arrays.

**Return value**

Return the values present in at least two arrays, in any order.

### Examples
**Example 1**

- Input: `nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]`
- Output: `[3,2]`

**Example 2**

- Input: `nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]`
- Output: `[2,3,1]`

**Example 3**

- Input: `nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]`
- Output: `[]`

---

## Solution
### Approach
Convert each array to a set so duplicates inside one array count once. Count in how many sets each value appears and return those with count at least two.

### Complexity Analysis
- **Time Complexity**: `O(n1 + n2 + n3)`
- **Space Complexity**: `O(n1 + n2 + n3)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
