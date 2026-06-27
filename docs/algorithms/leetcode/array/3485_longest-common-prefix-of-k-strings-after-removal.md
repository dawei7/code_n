# Longest Common Prefix of K Strings After Removal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3485 |
| Difficulty | Hard |
| Topics | Array, String, Trie |
| Official Link | [longest-common-prefix-of-k-strings-after-removal](https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/) |

## Problem Description & Examples
### Goal
Given a list of strings and an integer `k`, determine the length of the longest common prefix that can be formed by at least `k` strings after removing at most one character from each string.

### Function Contract
**Inputs**

- `strs`: A list of strings consisting of lowercase English letters.
- `k`: An integer representing the minimum number of strings that must share the resulting prefix.

**Return value**

- An integer representing the maximum possible length of a common prefix shared by at least `k` strings, where each string is allowed to have one character deleted.

### Examples
**Example 1**

- Input: `strs = ["flower","flow","flight"], k = 3`
- Output: `3`

**Example 2**

- Input: `strs = ["apple","apply","ape"], k = 2`
- Output: `4`

**Example 3**

- Input: `strs = ["dog","racecar","car"], k = 1`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a Trie (Prefix Tree) combined with a depth-first search (DFS) or a greedy approach. Since we can remove at most one character, for each string, we consider two states: "no character removed yet" and "one character already removed". We traverse the Trie while tracking how many strings reach each node under these two states.

---

## Complexity Analysis
- **Time Complexity**: `O(N * L)`, where `N` is the number of strings and `L` is the maximum length of a string. We process each character of each string to build/traverse the state-space.
- **Space Complexity**: `O(N * L)` to store the Trie structure representing the prefixes.
