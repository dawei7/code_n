# H-Index II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 275 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [h-index-ii](https://leetcode.com/problems/h-index-ii/) |

## Problem Description & Examples
### Goal
Given a list of citation counts sorted in ascending order, determine the researcher's H-index. The H-index is defined as the maximum value $h$ such that the researcher has published at least $h$ papers that have each been cited at least $h$ times.

### Function Contract
**Inputs**

- `citations`: A list of integers representing the number of citations for each paper, sorted in non-decreasing order.

**Return value**

- An integer representing the calculated H-index.

### Examples
**Example 1**

- Input: `citations = [0, 1, 3, 5, 6]`
- Output: `3`

**Example 2**

- Input: `citations = [1, 2, 100]`
- Output: `2`

**Example 3**

- Input: `citations = [10, 11, 12]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Binary Search. Since the input array is already sorted, we can leverage the property that for any index `i`, the number of papers with at least `citations[i]` citations is `n - i`. We search for the largest index `i` such that `citations[i] >= n - i`.

---

## Complexity Analysis
- **Time Complexity**: $O(\log n)$, where $n$ is the number of papers, due to the binary search approach.
- **Space Complexity**: $O(1)$, as we only use a constant amount of extra space for pointers.
