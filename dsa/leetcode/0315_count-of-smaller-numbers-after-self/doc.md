# Count of Smaller Numbers After Self

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 315 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |

## Problem Description
### Goal
Given an integer array `nums`, compute one result for every original position. For index `i`, count indices `j` satisfying both $j > i$ and `nums[j] < nums[i]`.

Return these counts in the same order and length as the input. Equal values to the right are not smaller and contribute nothing, while duplicate smaller occurrences at different positions each contribute once. The final position always has count zero, and a one-element input therefore returns `[0]`. Meet the required subquadratic complexity rather than comparing every index with every later index independently.

### Function Contract
**Inputs**

- `nums`: the integer array

**Return value**

An array of the same length where result position `i` is the number of indices $j > i$ satisfying `nums[j] < nums[i]`.

### Examples
**Example 1**

- Input: `nums = [5, 2, 6, 1]`
- Output: `[2, 1, 1, 0]`

**Example 2**

- Input: `nums = [-1]`
- Output: `[0]`

**Example 3**

- Input: `nums = [-1, -1]`
- Output: `[0, 0]`
