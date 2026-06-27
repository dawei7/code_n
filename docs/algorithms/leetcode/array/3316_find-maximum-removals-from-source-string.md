# Find Maximum Removals From Source String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3316 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, String, Dynamic Programming |
| Official Link | [find-maximum-removals-from-source-string](https://leetcode.com/problems/find-maximum-removals-from-source-string/) |

## Problem Description & Examples
### Goal
Given a source string `source`, a target string `pattern`, and an array of indices `targetIndices`, determine the maximum number of characters that can be removed from `source` such that `pattern` remains a subsequence of the modified `source`. A removal is only valid if the index of the character being removed is present in `targetIndices`.

### Function Contract
**Inputs**

- `source` (str): The original string.
- `pattern` (str): The string that must remain a subsequence.
- `targetIndices` (List[int]): A list of indices in `source` that are eligible for removal.

**Return value**

- `int`: The maximum number of characters that can be removed from `source` while keeping `pattern` as a subsequence.

### Examples
**Example 1**

- Input: `source = "abbaac", pattern = "aba", targetIndices = [0, 1, 2, 3, 4, 5]`
- Output: `2`

**Example 2**

- Input: `source = "bcda", pattern = "d", targetIndices = [0, 3]`
- Output: `2`

**Example 3**

- Input: `source = "dda", pattern = "dda", targetIndices = [0, 1, 2]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. We define `dp[i][j]` as the maximum number of removals possible using the first `i` characters of `source` to form the first `j` characters of `pattern`. For each character in `source`, we have two choices: either keep it (if it matches the current character in `pattern`) or remove it (if its index is in `targetIndices`).

---

## Complexity Analysis
- **Time Complexity**: `O(N * M)`, where `N` is the length of `source` and `M` is the length of `pattern`.
- **Space Complexity**: `O(N * M)` (can be optimized to `O(M)`), where `N` is the length of `source` and `M` is the length of `pattern`.
