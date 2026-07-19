# Max Chunks To Make Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 769 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Sorting, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-chunks-to-make-sorted/) |

## Problem Description

### Goal

Given an array `arr` that is a permutation of the integers from `0` through $n - 1$, divide it into consecutive, nonempty chunks covering the complete array. Sort each chunk independently and concatenate the results in the original chunk order.

Return the maximum number of chunks for which the final concatenation is the globally sorted increasing array. The permutation guarantee means every value occurs exactly once, and chunk boundaries must be cuts between adjacent original positions rather than arbitrary group assignments.

### Function Contract

**Inputs**

- `arr`: a nonempty permutation of `0, 1, ..., len(arr) - 1`.

**Return value**

- The largest number of chunks whose independently sorted concatenation equals the globally sorted array.

### Examples

**Example 1**

- Input: `arr = [4,3,2,1,0]`
- Output: `1`
- Explanation: No proper prefix contains exactly the values that belong in those positions.

**Example 2**

- Input: `arr = [1,0,2,3,4]`
- Output: `4`
- Explanation: `[1,0]`, `[2]`, `[3]`, and `[4]` can be sorted independently.

**Example 3**

- Input: `arr = [0,2,1,4,3]`
- Output: `3`
- Explanation: The maximum partition is `[0]`, `[2,1]`, and `[4,3]`.
