# Range Sum Query - Immutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 303 |
| Difficulty | Easy |
| Topics | Array, Design, Prefix Sum |
| Official Link | [range-sum-query-immutable](https://leetcode.com/problems/range-sum-query-immutable/) |

## Problem Description & Examples
### Goal
The objective is to design a data structure that efficiently calculates the sum of elements within a specific contiguous range of an integer array. Since the array is immutable (it does not change after initialization), we can pre-process the data to ensure that individual range sum queries are answered in constant time.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the immutable array.
- `queries`: A list of tuples/lists, where each element contains two integers `[left, right]` representing the inclusive indices of the range.

**Return value**

- A list of integers where each element corresponds to the sum of the array elements from index `left` to `right` (inclusive) for each query.

### Examples
**Example 1**

- Input: `nums = [-2, 0, 3, -5, 2, -1]`, `queries = [[0, 2], [2, 5], [0, 5]]`
- Output: `[1, -1, -3]`

**Example 2**

- Input: `nums = [1, 2]`, `queries = [[0, 0], [1, 1]]`
- Output: `[1, 2]`

**Example 3**

- Input: `nums = [5]`, `queries = [[0, 0]]`
- Output: `[5]`

---

## Underlying Base Algorithm(s)
The optimal approach utilizes the **Prefix Sum** technique. By constructing an auxiliary array where each index `i` stores the cumulative sum of the input array up to index `i-1`, any range sum `[L, R]` can be computed as `prefix_sum[R + 1] - prefix_sum[L]`. This transforms an O(N) summation into an O(1) subtraction.

---

## Complexity Analysis
- **Time Complexity**: O(N + Q), where N is the number of elements in the array (for pre-processing) and Q is the number of queries. Each query is answered in O(1) time.
- **Space Complexity**: O(N) to store the prefix sum array.
