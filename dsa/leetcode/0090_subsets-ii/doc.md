# Subsets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 90 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subsets-ii/) |

## Problem Description
### Goal
You are given a nonempty integer list that may contain repeated values. Form subsets by selecting any collection of input occurrences, including selecting none or all of them, without using one occurrence more than once.

Return every distinct value multiset that can result. Choosing a different copy of an equal value with the same selected multiplicity does not create another subset, so duplicates must be suppressed. The subsets and their values may appear in any order, and the empty subset appears exactly once.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list that may contain duplicates

**Return value**

A list of all unique subsets in any outer or inner ordering.

### Examples
**Example 1**

- Input: `nums = [1,2,2]`
- Output: `[[],[1],[1,2],[1,2,2],[2],[2,2]]` in any order

**Example 2**

- Input: `nums = [0]`
- Output: `[[],[0]]`

**Example 3**

- Input: `nums = [1,1]`
- Output: `[[],[1],[1,1]]`
