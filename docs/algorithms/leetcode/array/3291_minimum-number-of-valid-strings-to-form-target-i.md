# Minimum Number of Valid Strings to Form Target I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3291 |
| Difficulty | Medium |
| Topics | Array, String, Binary Search, Dynamic Programming, Greedy, Trie, Segment Tree, Rolling Hash, String Matching, Hash Function |
| Official Link | [minimum-number-of-valid-strings-to-form-target-i](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/) |

## Problem Description & Examples
### Goal
Given a list of available strings and a target string, determine the minimum number of concatenated substrings (each taken from the available list) required to construct the target string exactly. If it is impossible to form the target, return -1.

### Function Contract
**Inputs**

- `words`: A list of strings representing the available building blocks.
- `target`: The string that needs to be constructed.

**Return value**

- An integer representing the minimum number of concatenated substrings needed, or -1 if the target cannot be formed.

### Examples
**Example 1**

- Input: `words = ["abc","aaaaa","bcfg"], target = "abcdabc"`
- Output: `3`

**Example 2**

- Input: `words = ["ab","abab"], target = "ababa"`
- Output: `2`

**Example 3**

- Input: `words = ["ax","ay","bx","by"], target = "axby"`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using a Trie (Prefix Tree) to store all available words, combined with Dynamic Programming. The DP state `dp[i]` represents the minimum number of substrings needed to form the prefix of `target` of length `i`. For each position `i`, we traverse the Trie to find the longest prefix of `target[i:]` that exists as a substring in any of the `words`.

---

## Complexity Analysis
- **Time Complexity**: `O(N * L + M * L)`, where `N` is the number of words, `L` is the average length of words, and `M` is the length of the target. We build the Trie in `O(N * L)` and perform DP with Trie traversal in `O(M * L)`.
- **Space Complexity**: `O(N * L)` to store the Trie structure.
