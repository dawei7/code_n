# Truncate Sentence

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/truncate-sentence/) |
| Frontend ID | 1816 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A sentence is a sequence of words separated by exactly one space. It has no space before its first word or after its last word, and every word contains only uppercase or lowercase English letters. Thus, spaces are precisely the boundaries between consecutive words; punctuation and repeated separators do not occur.

Given such a sentence `s` and an integer `k`, retain the first `k` words in their original order and discard every later word. The value of `k` is at least 1 and does not exceed the number of words in `s`. Return the resulting sentence, preserving the single spaces between the retained words.

### Function Contract

**Inputs**

- `s`: a valid sentence with $1 \le \lvert s \rvert \le 500$, made only of English letters and single spaces, with no leading or trailing space.
- `k`: an integer from 1 through the number of words in `s`.
- Let $n = \lvert s \rvert$.

**Return value**

- Return the prefix of `s` containing exactly its first `k` words, without a trailing space.

### Examples

**Example 1**

- Input: `s = "Hello how are you Contestant", k = 4`
- Output: `"Hello how are you"`

The fourth word ends before `"Contestant"`, so that later word and its preceding separator are excluded.

**Example 2**

- Input: `s = "What is the solution to this problem", k = 4`
- Output: `"What is the solution"`

**Example 3**

- Input: `s = "chopper is not a tanuki", k = 5`
- Output: `"chopper is not a tanuki"`

Here `k` equals the sentence's word count, so the complete sentence remains.
