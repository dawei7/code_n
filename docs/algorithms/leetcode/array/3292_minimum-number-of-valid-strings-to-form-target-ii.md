# Minimum Number of Valid Strings to Form Target II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3292 |
| Difficulty | Hard |
| Topics | Array, String, Binary Search, Dynamic Programming, Greedy, Segment Tree, Rolling Hash, String Matching, Hash Function |
| Official Link | [minimum-number-of-valid-strings-to-form-target-ii](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/) |

## Problem Description & Examples
### Goal
Given a list of available strings and a target string, determine the minimum number of valid strings (prefixes of the provided words) required to concatenate and form the target string. If it is impossible to construct the target, return -1.

### Function Contract
**Inputs**

- `words`: A list of strings representing the available building blocks.
- `target`: The string that needs to be constructed.

**Return value**

- An integer representing the minimum number of concatenated prefixes needed, or -1 if construction is impossible.

### Examples
**Example 1**

- Input: `words = ["abc","aaaaa","bcfg"], target = "abcdabc"`
- Output: `3`

**Example 2**

- Input: `words = ["ab","abab"], target = "ababa"`
- Output: `2`

**Example 3**

- Input: `words = ["abcdef"], target = "xyz"`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of a **Trie** (to store prefixes of `words`) and **Dynamic Programming** (to find the minimum count). To optimize the search for the longest prefix match at each position, we use the Trie to find the maximum length `k` such that `target[i:i+k]` is a prefix of some word in `words`. We then use a greedy approach with DP or a jump-table strategy to minimize the total segments.

---

## Complexity Analysis
- **Time Complexity**: `O(N * L + M * log(max_len))`, where `N` is the number of words, `L` is the average length of words, `M` is the length of the target, and `max_len` is the maximum length of a word.
- **Space Complexity**: `O(N * L)` to store the Trie structure.
