# Max Chunks To Make Sorted II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 768 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Sorting, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/) |

## Problem Description

### Goal

Given an integer array `arr` that may contain duplicate values, split it into consecutive, nonempty chunks covering every element exactly once. Sort each chunk independently and concatenate the sorted chunks in their original chunk order.

Return the maximum number of chunks for which that concatenation equals the result of sorting the entire array. Chunk boundaries must be contiguous cuts in `arr`; elements cannot be assigned to arbitrary groups, and equal values at different positions remain separate occurrences.

### Function Contract

**Inputs**

- `arr`: a nonempty integer array that may contain duplicate values.

**Return value**

- The maximum number of chunks satisfying the independent-sorting condition.

### Examples

**Example 1**

- Input: `arr = [5,4,3,2,1]`
- Output: `1`
- Explanation: Every earlier cut would leave a larger value before a smaller value, so the whole array must be one chunk.

**Example 2**

- Input: `arr = [2,1,3,4,4]`
- Output: `4`
- Explanation: The chunks `[2,1]`, `[3]`, `[4]`, and `[4]` independently sort to the global order.

**Example 3**

- Input: `arr = [1,1,0,0,1]`
- Output: `2`
- Explanation: Cutting before the final `1` is valid, while duplicates and smaller zeros prevent earlier cuts.
