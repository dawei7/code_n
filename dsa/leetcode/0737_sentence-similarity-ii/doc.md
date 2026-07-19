# Sentence Similarity II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 737 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find |
| Official Link | [LeetCode](https://leetcode.com/problems/sentence-similarity-ii/) |

## Problem Description
### Goal
Given two sentences as arrays of words and a list of similar-word pairs, determine whether the sentences are similar. They must have the same number of words and are compared at matching positions.

Similarity is reflexive, symmetric, and transitive: a word is similar to itself, pair direction does not matter, and a chain of listed relationships places all connected words in one similarity group. Return `True` only when every aligned word pair is identical or connected through such a group; otherwise return `False`.

### Function Contract
**Inputs**

- `sentence1`: the first ordered list of words
- `sentence2`: the second ordered list of words
- `similarPairs`: word pairs that connect words into similarity groups

**Return value**

- `True` exactly when the sentences have equal length and each aligned pair contains identical words or words connected through one similarity group

### Examples
**Example 1**

- Input: `sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]`
- Output: `true`

**Example 2**

- Input: `sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]`
- Output: `true`

**Example 3**

- Input: `sentence1 = ["great"], sentence2 = ["fine"], similarPairs = [["great","good"],["fine","excellent"]]`
- Output: `false`
