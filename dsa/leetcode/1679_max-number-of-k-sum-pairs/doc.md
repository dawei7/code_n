# Max Number of K-Sum Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1679 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-number-of-k-sum-pairs/) |

## Problem Description
### Goal

Given an integer array `nums` and an integer target `k`, an operation chooses two currently present elements whose values sum to exactly `k` and removes both. Removed elements cannot participate in later operations, while duplicate values are separate elements and may support several different removals.

Return the maximum number of operations that can be performed. The order of the original array does not restrict which elements may be paired, and the specific pairs do not need to be returned. The objective is therefore to form as many disjoint value-complement pairs as the available multiplicities permit.

### Function Contract
**Inputs**

- `nums`: a list of $n$ positive integers, each representing one independently removable element
- `k`: the exact sum required for every removed pair

**Return value**

The maximum number of disjoint pairs from `nums` whose two values sum to `k`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4], k = 5`
- Output: `2`

**Example 2**

- Input: `nums = [3,1,3,4,3], k = 6`
- Output: `1`

**Example 3**

- Input: `nums = [2,2,2,3,1,1,4], k = 4`
- Output: `2`
