# Sentence Similarity III

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sentence-similarity-iii/) |
| Frontend ID | 1813 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each of `sentence1` and `sentence2` is a non-empty sequence of words. Words contain only uppercase and lowercase English letters, consecutive words are separated by exactly one space, and neither sentence has leading or trailing spaces.

The sentences are similar when an arbitrary sentence, possibly empty, can be inserted at one word boundary inside either original sentence to make the two strings equal. The inserted words must remain separated from existing words by spaces; characters cannot be inserted into an existing word. Return whether one permitted insertion can make `sentence1` and `sentence2` identical.

### Function Contract

**Inputs**

- `sentence1`, `sentence2`: valid sentence strings whose lengths are each from 1 through 100 characters.
- Let $n$ and $m$ be their respective numbers of words.
- Word comparison is case-sensitive.

**Return value**

- Return `true` if the longer sentence can be obtained by inserting one contiguous sequence of whole words into the shorter sentence.
- The inserted sequence may be empty or may occur before the first word, between two words, or after the last word.
- Return `false` otherwise.

### Examples

**Example 1**

- Input: `sentence1 = "My name is Haley", sentence2 = "My Haley"`
- Output: `true`

Insert `"name is"` between the two words of `sentence2`.

**Example 2**

- Input: `sentence1 = "of", sentence2 = "A lot of words"`
- Output: `false`

The shorter word matches an interior word, leaving unmatched words on both sides; one insertion cannot preserve the shorter sentence's order at a single boundary.

**Example 3**

- Input: `sentence1 = "Eating right now", sentence2 = "Eating"`
- Output: `true`

Insert `"right now"` after the shorter sentence.
