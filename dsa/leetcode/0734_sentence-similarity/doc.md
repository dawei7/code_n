# Sentence Similarity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 734 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/sentence-similarity/) |

## Problem Description
### Goal
Given two sentences represented as arrays of words and a list of unordered similar-word pairs, determine whether the sentences are similar. Similar sentences must contain the same number of words and are compared at matching positions.

At every position, the two words must either be identical or appear together in one explicitly listed pair. Direct similarity is symmetric but not transitive for this problem: two separate listed links do not imply a third relationship through an intermediate word. Return `True` only when every aligned position satisfies the rule.

### Function Contract
**Inputs**

- `sentence1`: the first ordered list of words
- `sentence2`: the second ordered list of words
- `similarPairs`: unordered word pairs that are declared directly similar

**Return value**

- `True` exactly when the sentences have the same number of words and all aligned positions satisfy the direct similarity rule

### Examples
**Example 1**

- Input: `sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]`
- Output: `true`

**Example 2**

- Input: `sentence1 = ["great"], sentence2 = ["great"], similarPairs = []`
- Output: `true`

**Example 3**

- Input: `sentence1 = ["great"], sentence2 = ["fine"], similarPairs = [["great","good"],["good","fine"]]`
- Output: `false`
