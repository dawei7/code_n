# Top K Frequent Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 347 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Heap, Bucket Sort, Counting, Quickselect |
| Official Link | [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) |

## Problem Description
### Goal
Given a nonempty integer array and a valid count `k`, measure the occurrence frequency of every distinct value. Select exactly the `k` values having the greatest frequencies, with the input guarantee ensuring a unique qualifying set at the cutoff.

Return those distinct values in any order, listing each once regardless of its source count. Negative values and zero participate normally, and duplicate occurrences affect frequency rather than output multiplicity. Meet the required complexity better than sorting all input occurrences or all distinct values by frequency. The function returns the values themselves, not their counts.

### Function Contract
**Inputs**

- `nums`: a non-empty list of integers
- `k`: the number of most-frequent distinct values to return

**Return value**

- A list containing exactly the `k` values with the greatest occurrence counts, in any order.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 2, 2, 3], k = 2`
- Output: `[1, 2]`

**Example 2**

- Input: `nums = [1], k = 1`
- Output: `[1]`

**Example 3**

- Input: `nums = [4, 4, 4, 4, 2, 2, 2, 3], k = 2`
- Output: `[4, 2]`
