# Longest Unequal Adjacent Groups Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2901 |
| Difficulty | Medium |
| Topics | Array, String, Dynamic Programming |
| Official Link | [longest-unequal-adjacent-groups-subsequence-ii](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/) |

## Problem Description & Examples
### Goal
Given two arrays of strings and integers, find the longest subsequence such that no two adjacent elements in the subsequence belong to different groups (as defined by the integer array) and satisfy a specific similarity condition: the strings must have the same length and differ by exactly one character (Hamming distance of 1).

### Function Contract
**Inputs**

- `words`: A list of strings representing the available elements.
- `groups`: A list of integers where `groups[i]` is the group ID of `words[i]`.

**Return value**

- A list of strings representing the longest valid subsequence found.

### Examples
**Example 1**

- Input: `words = ["e","a","b"], groups = [0,0,1]`
- Output: `["e","b"]`

**Example 2**

- Input: `words = ["bab","dab","cab"], groups = [1,2,2]`
- Output: `["bab","cab"]`

**Example 3**

- Input: `words = ["a","b","c","d"], groups = [1,2,3,4]`
- Output: `["a","b","c","d"]`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. We maintain a `dp` array where `dp[i]` stores the length of the longest valid subsequence ending at index `i`. To reconstruct the path, we store a `parent` array. The transition condition checks if `groups[i] != groups[j]` and if `words[i]` and `words[j]` have the same length and a Hamming distance of exactly 1.

---

## Complexity Analysis
- **Time Complexity**: O(n² * L), where n is the number of words and L is the maximum length of a word, due to the nested loops and the string comparison.
- **Space Complexity**: O(n) to store the DP table and the parent pointers.
