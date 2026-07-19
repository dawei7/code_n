# Prefix and Suffix Search

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 745 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Design, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/prefix-and-suffix-search/) |

## Problem Description
### Goal
Design `WordFilter` from an indexed array `words`. For each query `f(pref, suff)`, find words that begin with the complete string `pref` and end with the complete string `suff` at the same time.

Return the largest original index among all matching words, or `-1` when no word satisfies both conditions. Repeated word values remain distinct indexed entries, and every query is independent; querying does not change the word list or its indices.

### Function Contract
**Inputs**

- `operations`: a constructor call `"WordFilter"` followed by zero or more `"f"` queries
- `arguments`: constructor arguments containing the word list, then `[prefix, suffix]` for each query

**Return value**

- `None` for construction and one integer per query: the maximum matching original index, or `-1`

### Examples
**Example 1**

- Input: `operations = ["WordFilter","f"], arguments = [[["apple"]],["a","e"]]`
- Output: `[null,0]`

**Example 2**

- Input: `operations = ["WordFilter","f","f"], arguments = [[["apple","apply","ape"]],["ap","e"],["app","ly"]]`
- Output: `[null,2,1]`

**Example 3**

- Input: `operations = ["WordFilter","f"], arguments = [[["test","team"]],["x","z"]]`
- Output: `[null,-1]`
