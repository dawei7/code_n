# Word Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 425 |
| Difficulty | Hard |
| Topics | Array, String, Backtracking, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/word-squares/) |

## Problem Description
### Goal
Given unique lowercase words of one common length `n`, construct ordered sequences of exactly `n` words. A sequence is a word square when its character grid is symmetric: for every valid pair of indices, character `j` of word `i` equals character `i` of word `j`.

Return every word square formable from the supplied words in any order. A dictionary word may be selected more than once within one square, and different row orders can create different results. Every row and corresponding column must spell the same complete word; matching only prefixes before the final row is not enough.

### Function Contract
**Inputs**

- `words`: a list of distinct lowercase words, all having the same length

**Return value**

- Return every word square that can be formed from the supplied words; a word may be selected more than once, and the squares may be returned in any order.

### Examples
**Example 1**

- Input: `words = ["area", "lead", "wall", "lady", "ball"]`
- Output: `[["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]]`

**Example 2**

- Input: `words = ["abat", "baba", "atan", "atal"]`
- Output: `[["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]]`

**Example 3**

- Input: `words = ["a"]`
- Output: `[["a"]]`
