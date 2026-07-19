# Two Sum II - Input Array Is Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 167 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |

## Problem Description
### Goal
Given a one-indexed array of integers sorted in non-decreasing order, find two positions whose values add exactly to `target`. The first chosen position must precede the second, and the input guarantee states that exactly one valid pair exists.

Return the two one-based indices as `[index1, index2]` with `index1 < index2`. Duplicate values may supply the pair when they occur at separate positions, but you may not use the same element twice. Preserve the sorted input and meet the constant-extra-space requirement; the output contains indices rather than the matched values.

### Function Contract
**Inputs**

- `numbers`: a nondecreasing list of integers
- `target`: required sum of exactly two distinct positions

**Return value**

The pair of one-based indices `[index1, index2]` with `index1 < index2`.

### Examples
**Example 1**

- Input: `numbers = [2,7,11,15], target = 9`
- Output: `[1,2]`

**Example 2**

- Input: `numbers = [2,3,4], target = 6`
- Output: `[1,3]`

**Example 3**

- Input: `numbers = [-1,0], target = -1`
- Output: `[1,2]`
