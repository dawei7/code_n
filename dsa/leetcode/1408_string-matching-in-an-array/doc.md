# String Matching in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1408 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/string-matching-in-an-array/) |

## Problem Description

### Goal

Given an array `words` of distinct lowercase English strings, identify every array entry that occurs as a contiguous substring of a different entry in the same array.

Return all qualifying words. Each word appears at most once because the input strings are distinct, and the result may be returned in any order. A word does not qualify merely by being a substring of itself.

### Function Contract

**Inputs**

- `words`: an array of $n$ distinct lowercase strings, where $1 \le n \le 100$ and every word has length from 1 through 30.

Let $L$ be the maximum word length.

**Return value**

- The words that occur contiguously inside at least one other array word, in any order.

### Examples

**Example 1**

- Input: `words = ["mass","as","hero","superhero"]`
- Output: `["as","hero"]`

**Example 2**

- Input: `words = ["leetcode","et","code"]`
- Output: `["et","code"]`

**Example 3**

- Input: `words = ["blue","green","red"]`
- Output: `[]`
