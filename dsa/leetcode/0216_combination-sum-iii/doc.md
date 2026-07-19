# Combination Sum III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 216 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/combination-sum-iii/) |

## Problem Description
### Goal
Choose exactly `k` distinct integers from the fixed set `1` through `9` so that their sum is exactly `n`. Each available number may appear at most once in a combination, and selection order does not create a different combination.

Return every valid combination exactly once, writing the values inside each combination in increasing order. The outer result may appear in any order. Exclude selections with too few or too many values even if their sum matches, and return an empty list when no size-`k` subset reaches `n`. Values outside `1..9`, repeated selections, and permutations of an existing combination are not valid additions.

### Function Contract
**Inputs**

- `k`: required number of selected values
- `n`: required sum

**Return value**

All valid increasing combinations, each once.

### Examples
**Example 1**

- Input: `k = 3, n = 7`
- Output: `[[1,2,4]]`

**Example 2**

- Input: `k = 3, n = 9`
- Output: `[[1,2,6],[1,3,5],[2,3,4]]`

**Example 3**

- Input: `k = 4, n = 1`
- Output: `[]`
