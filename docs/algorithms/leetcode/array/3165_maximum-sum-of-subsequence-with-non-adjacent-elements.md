# Maximum Sum of Subsequence With Non-adjacent Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3165 |
| Difficulty | Hard |
| Topics | Array, Divide and Conquer, Dynamic Programming, Segment Tree |
| Official Link | [maximum-sum-of-subsequence-with-non-adjacent-elements](https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/) |

## Problem Description & Examples
### Goal
Given an array of integers and a series of point updates, calculate the maximum sum of a subsequence such that no two elements in the subsequence are adjacent in the original array. After each update, return the total sum of these maximums across all queries, modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `queries`: A list of lists, where each `queries[i]` contains `[index, val]`, representing an update to set `nums[index] = val`.

**Return value**

- An integer representing the sum of the maximum non-adjacent subsequence sums after each query, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [3, 5, 9], queries = [[1, -2], [0, -3]]`
- Output: `21`
- Explanation: After [1, -2], nums is [3, -2, 9], max sum is 12. After [0, -3], nums is [-3, -2, 9], max sum is 9. 12 + 9 = 21.

**Example 2**

- Input: `nums = [0, -1], queries = [[0, -5]]`
- Output: `0`

**Example 3**

- Input: `nums = [2, 1, 4, 9], queries = [[3, 0], [1, 0]]`
- Output: `16`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Segment Tree**. Each node in the tree stores four values representing the maximum non-adjacent subsequence sum for its range:
1. `v00`: Neither the first nor the last element of the range is included.
2. `v01`: The last element is included, but the first is not.
3. `v10`: The first element is included, but the last is not.
4. `v11`: Both the first and last elements are included.
Merging two nodes involves combining these states while ensuring the non-adjacency constraint is maintained at the boundary.

---

## Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`, where N is the length of the array and Q is the number of queries. Each update takes logarithmic time to traverse the segment tree.
- **Space Complexity**: `O(N)` to store the segment tree nodes.
