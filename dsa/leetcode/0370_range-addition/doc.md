# Range Addition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 370 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/range-addition/) |

## Problem Description
### Goal
Begin with an integer array of the requested `length`, initialized entirely to zero. Each update `[start, end, increment]` adds `increment` to every position from `start` through `end`, including both endpoints.

Apply all updates cumulatively and return the final array. Ranges may overlap, increments may be positive or negative, and an index receives the sum of every update covering it. Updates do not overwrite earlier values, and no per-update output is needed. With no updates, return the requested number of zeroes unchanged. Meet the linear aggregate target rather than visiting every index in every range separately.

### Function Contract
**Inputs**

- `length`: the non-negative length of the result array
- `updates`: a list of triples `[start, end, increment]` describing inclusive index ranges

**Return value**

- The length-`length` array after all additions have been accumulated.

### Examples
**Example 1**

- Input: `length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]`
- Output: `[-2,0,3,5,3]`

**Example 2**

- Input: `length = 3, updates = [[0,2,1]]`
- Output: `[1,1,1]`

**Example 3**

- Input: `length = 1, updates = []`
- Output: `[0]`
