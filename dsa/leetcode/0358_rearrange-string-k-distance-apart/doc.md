# Rearrange String k Distance Apart

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 358 |
| Difficulty | Hard |
| Topics | Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/rearrange-string-k-distance-apart/) |

## Problem Description
### Goal
Given a nonempty lowercase string `s` and a nonnegative integer `k`, rearrange all character occurrences. In a valid result, any two equal characters occupy indices whose difference is at least `k`.

Return any valid permutation of the complete input multiset, or `""` when no such arrangement exists. Every occurrence must be used exactly once, and different letters have no separation requirement. When `k` is `0` or `1`, every permutation satisfies the distance rule, so the original string is acceptable. Do not return a partial arrangement merely because the remaining characters cannot be placed.

### Function Contract
**Inputs**

- `s`: a non-empty string of lowercase English letters
- `k`: a non-negative minimum distance between equal letters

**Return value**

- A permutation of `s` satisfying the distance rule, or `""` if no valid permutation exists.

### Examples
**Example 1**

- Input: `s = "aabbcc", k = 3`
- Output: `"abcabc"`

**Example 2**

- Input: `s = "aaabc", k = 3`
- Output: `""`

**Example 3**

- Input: `s = "aaadbbcc", k = 2`
- Output: `"abacabcd"`
