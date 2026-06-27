# Count Prefix and Suffix Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3045 |
| Difficulty | Hard |
| Topics | Array, String, Trie, Rolling Hash, String Matching, Hash Function |
| Official Link | [count-prefix-and-suffix-pairs-ii](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/) |

## Problem Description & Examples
### Goal
Given an array of strings, identify the total number of index pairs (i, j) such that i < j and the string at index i is both a prefix and a suffix of the string at index j.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.

**Return value**

- An integer representing the total count of valid pairs (i, j) where `words[i]` is a prefix and suffix of `words[j]`.

### Examples
**Example 1**

- Input: `words = ["a","aba","ababa","aa"]`
- Output: `4`

**Example 2**

- Input: `words = ["pa","papa","ma","mama"]`
- Output: `2`

**Example 3**

- Input: `words = ["abab","ab"]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is efficiently solved using a **Trie (Prefix Tree)**. Since we need to check if `words[i]` is both a prefix and a suffix of `words[j]`, we can represent the prefix-suffix pair as a tuple of characters `(words[j][k], words[j][n-len(words[j])+k])`. By inserting these pairs into a Trie as we iterate through the array, we can count how many previously seen strings match the current string's prefix-suffix structure in linear time relative to the total number of characters.

---

## Complexity Analysis
- **Time Complexity**: `O(N * L)`, where `N` is the number of words and `L` is the maximum length of a word. We iterate through each word once and perform constant-time Trie operations for each character.
- **Space Complexity**: `O(N * L)` in the worst case to store the Trie nodes representing the prefix-suffix pairs.
