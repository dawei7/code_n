# Patching Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 330 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/patching-array/) |

## Problem Description
### Goal
Given an array `nums` of positive integers sorted in ascending order and a positive bound `n`, you may add new positive integers to the array. After patching, every target value from `1` through `n` must be representable as the sum of some subset of the available occurrences.

Return the minimum number of added values needed to guarantee this complete coverage. Each original or patched occurrence can be used at most once within a particular subset sum, though different targets choose subsets independently. Values larger than the currently uncovered gap cannot create that missing smaller sum. Return only the patch count, not the added values or all representing subsets.

### Function Contract
**Inputs**

- `nums`: a sorted list of positive integers
- `n`: the inclusive upper bound of the sums that must be representable

**Return value**

The minimum number of added values required to make every sum in `[1, n]` representable.

### Examples
**Example 1**

- Input: `nums = [1,3], n = 6`
- Output: `1`

**Example 2**

- Input: `nums = [1,5,10], n = 20`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,2], n = 5`
- Output: `0`
