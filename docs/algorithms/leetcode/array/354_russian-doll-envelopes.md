# Russian Doll Envelopes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 354 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Official Link | [russian-doll-envelopes](https://leetcode.com/problems/russian-doll-envelopes/) |

## Problem Description & Examples
### Goal
Given a collection of envelopes represented by pairs of integers `(width, height)`, determine the maximum number of envelopes you can nest inside one another. An envelope can fit into another if and only if both its width and height are strictly greater than the width and height of the inner envelope. You may rotate an envelope (not applicable here as dimensions are fixed) but you cannot rotate them to change their orientation; you must fit them based on the provided dimensions.

### Function Contract
**Inputs**

- `envelopes`: A list of lists, where each inner list contains two integers `[width, height]`.

**Return value**

- An integer representing the maximum number of envelopes that can be nested.

### Examples
**Example 1**

- Input: `[[5,4],[6,4],[6,7],[2,3]]`
- Output: `3`
- Explanation: The envelopes can be nested as `[2,3] => [5,4] => [6,7]`.

**Example 2**

- Input: `[[1,1],[1,1],[1,1]]`
- Output: `1`

**Example 3**

- Input: `[[4,5],[4,6],[6,7],[2,3],[1,1]]`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is a variation of the "Longest Increasing Subsequence" (LIS) problem. By sorting the envelopes primarily by width in ascending order and secondarily by height in descending order, we reduce the problem to finding the LIS of the heights. The descending sort on height ensures that for envelopes with the same width, we cannot pick more than one, as their heights will be in non-increasing order, preventing a strictly increasing sequence.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of envelopes. Sorting takes `O(N log N)`, and the LIS algorithm using binary search takes `O(N log N)`.
- **Space Complexity**: `O(N)` to store the auxiliary array used for the binary search approach to LIS.
