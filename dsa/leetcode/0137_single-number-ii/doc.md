# Single Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 137 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/single-number-ii/) |

## Problem Description
### Goal
Given a nonempty list of integers, exactly one value appears once while every other distinct value appears exactly three times. The three matching occurrences may be separated and arranged in any order throughout the list.

Return the lone value, including when that value is negative or zero. The result is the integer itself rather than an index, and the input guarantee rules out multiple singletons or incomplete triples. Meet the intended linear running time and constant-extra-space requirements rather than storing a full frequency table whose size grows with the number of distinct input values.

### Function Contract
**Inputs**

- `nums`: integers satisfying the triples-plus-one frequency guarantee

**Return value**

The unique value that occurs once.

### Examples
**Example 1**

- Input: `nums = [2,2,3,2]`
- Output: `3`

**Example 2**

- Input: `nums = [0,1,0,1,0,1,99]`
- Output: `99`

**Example 3**

- Input: `nums = [-2,-2,4,-2]`
- Output: `4`
