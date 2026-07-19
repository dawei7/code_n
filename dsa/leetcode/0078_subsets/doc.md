# Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 78 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subsets/) |

## Problem Description
### Goal
You are given an array `nums` of unique integers. A subset chooses any collection of those values, from choosing none through choosing every value, without using an element more than once.

Return the complete power set containing all $2^{n}$ unique subsets. The empty subset and full input set must each appear exactly once. Value order inside a subset does not create another answer, and the solution set may be returned in any order.

### Function Contract
**Inputs**

- `nums`: a list of distinct integers

**Return value**

A `List[List[int]]` containing all $2^{n}$ subsets.

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]` in any order

**Example 2**

- Input: `nums = [0]`
- Output: `[[],[0]]`

**Example 3**

- Input: `nums = [-1,2]`
- Output: `[[],[-1],[2],[-1,2]]` in any order
