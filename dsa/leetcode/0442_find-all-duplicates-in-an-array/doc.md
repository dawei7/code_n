# Find All Duplicates in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 442 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/) |

## Problem Description
### Goal
Given an integer array `nums` of length `n`, every value lies in the range `1..n` and occurs either once or twice. Identify the values having a second occurrence, regardless of where the two positions appear.

Return every duplicated value once, in any order. Values occurring once must be excluded, and the frequency guarantee rules out larger counts. Meet the required linear running time with constant auxiliary space beyond the output; modifying the input array to record visits is allowed. The result contains values rather than duplicate indices or all repeated occurrences.

### Function Contract
**Inputs**

- `nums`: an integer array of length `n` whose values lie in `[1, n]` and occur at most twice

**Return value**

- Return all values occurring twice, in any order. The input array may be modified.

### Examples
**Example 1**

- Input: `nums = [4, 3, 2, 7, 8, 2, 3, 1]`
- Output: `[2, 3]`

**Example 2**

- Input: `nums = [1, 1, 2]`
- Output: `[1]`

**Example 3**

- Input: `nums = [1]`
- Output: `[]`
