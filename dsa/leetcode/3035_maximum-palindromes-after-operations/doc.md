# Maximum Palindromes After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3035 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Greedy, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-palindromes-after-operations/) |

## Problem Description

### Goal

You are given a 0-indexed array `words` containing $n$ 0-indexed lowercase strings. An operation chooses two word indices `i` and `j`, a valid character position `x` in `words[i]`, and a valid character position `y` in `words[j]`, then swaps those two characters. The word indices may be equal.

You may perform this operation any number of times, including zero. Consequently, characters can be redistributed among positions while every word keeps its original length and the total frequency of each letter remains unchanged.

Return the maximum number of strings in `words` that can simultaneously be palindromes after the swaps.

### Function Contract

Let $n=\lvert\texttt{words}\rvert$ and let

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert
$$

be the total number of characters.

**Inputs**

- `words`: An array with $1 \le n \le 1000$; every word has length from $1$ through $100$ and contains only lowercase English letters.

**Return value**

Return the greatest number of words that can be made palindromic at the same time while preserving all word lengths and global character frequencies.

### Examples

#### Example 1

- **Input:** `words = ["abbb","ba","aa"]`
- **Output:** `3`
- **Explanation:** The characters can be rearranged into `"bbbb"`, `"aa"`, and `"aa"`, so every word becomes a palindrome.

#### Example 2

- **Input:** `words = ["abc","ab"]`
- **Output:** `2`
- **Explanation:** The available letters can form the palindromes `"aca"` and `"bb"`.

#### Example 3

- **Input:** `words = ["cd","ef","a"]`
- **Output:** `1`
- **Explanation:** The one-character word is already a palindrome, while the four other letters contain no equal pair for either length-two word.
