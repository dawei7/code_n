# Create Sorted Array through Instructions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1649 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [create-sorted-array-through-instructions](https://leetcode.com/problems/create-sorted-array-through-instructions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/create-sorted-array-through-instructions/).

### Goal
Insert numbers one by one into a growing sorted array. Each insertion costs the
smaller of the count of existing values less than the number and the count of
existing values greater than it.

### Function Contract
**Inputs**

- `instructions`: values inserted in order.

**Return value**

The total insertion cost modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `instructions = [1, 5, 6, 2]`
- Output: `1`

**Example 2**

- Input: `instructions = [1, 2, 3, 6, 5, 4]`
- Output: `3`

**Example 3**

- Input: `instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]`
- Output: `4`

---

## Solution
### Approach
Use a Fenwick tree or segment tree over value frequencies. Before inserting
`x`, query how many inserted values are `< x` and how many are `> x`; add the
smaller count to the answer, then update the frequency of `x`.

### Complexity Analysis
- **Time Complexity**: `O(n log M)`, where `M` is the maximum instruction value.
- **Space Complexity**: `O(M)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
