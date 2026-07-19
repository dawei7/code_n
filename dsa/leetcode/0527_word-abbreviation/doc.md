# Word Abbreviation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 527 |
| Difficulty | Hard |
| Topics | Array, String, Greedy, Trie, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/word-abbreviation/) |

## Problem Description
### Goal
Given a list of distinct lowercase words, abbreviate a word by retaining a nonempty prefix and its final character while replacing the omitted middle run with that run's decimal length. Do not abbreviate when the resulting text would be no shorter than the original word.

Return one abbreviation per input position in the same order. All returned abbreviations must be unique within the list; when two words collide, lengthen their retained prefixes only as far as needed to distinguish them. For each word, use the shortest valid abbreviation under those rules, and leave a word unchanged when no shorter unique form exists.

### Function Contract
**Inputs**

- `words`: a list of distinct lowercase words

**Return value**

- The required abbreviation for each word, preserving the input order

### Examples
**Example 1**

- Input: `words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]`
- Output: `["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"]`

**Example 2**

- Input: `words = ["abcdef", "abqdef"]`
- Output: `["abc2f", "abq2f"]`

**Example 3**

- Input: `words = ["localization"]`
- Output: `["l10n"]`
