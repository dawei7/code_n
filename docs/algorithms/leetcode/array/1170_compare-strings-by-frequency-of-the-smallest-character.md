# Compare Strings by Frequency of the Smallest Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1170 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Binary Search, Sorting |
| Official Link | [compare-strings-by-frequency-of-the-smallest-character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/) |

## Problem Description & Examples
### Goal
For each query string, count how many word strings have a larger frequency of their smallest character.

### Function Contract
**Inputs**

- `queries`: query strings.
- `words`: comparison strings.

**Return value**

Array where each entry is the number of words with `f(word) > f(query)`, where `f(s)` counts occurrences of the lexicographically smallest character in `s`.

### Examples
**Example 1**

- Input: `queries = ["cbd"]`, `words = ["zaaaz"]`
- Output: `[1]`

**Example 2**

- Input: `queries = ["bbb","cc"]`, `words = ["a","aa","aaa","aaaa"]`
- Output: `[1,2]`

**Example 3**

- Input: `queries = ["abcd","aabb"]`, `words = ["zzzz","abc","aa"]`
- Output: `[2,1]`

---

## Underlying Base Algorithm(s)
Frequency transform, sorting, and binary search.

---

## Complexity Analysis
- **Time Complexity**: `O((q + w) * L + w log w + q log w)` where `L` is max string length.
- **Space Complexity**: `O(w)`
