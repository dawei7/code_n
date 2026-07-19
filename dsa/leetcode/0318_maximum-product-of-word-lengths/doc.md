# Maximum Product of Word Lengths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 318 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-word-lengths/) |

## Problem Description
### Goal
Given a list of lowercase words, choose two different list positions whose words share no letter. Repeated occurrences of a letter inside one word affect its length but do not create additional character types for the disjointness test.

Return the maximum product of the two selected word lengths. Different words may have equal text or length, but a pair qualifies only when their sets of letters are disjoint. If no valid pair exists, return `0`. The function returns only the largest product, not the selected words or their indices, and every pair must use two different positions from the supplied list.

### Function Contract
**Inputs**

- `words`: a list of strings containing lowercase English letters

**Return value**

The largest product `len(words[i]) * len(words[j])` over pairs with no shared letter, or zero if no such pair exists.

### Examples
**Example 1**

- Input: `words = ["abcw","baz","foo","bar","xtfn","abcdef"]`
- Output: `16`

**Example 2**

- Input: `words = ["a","ab","abc","d","cd","bcd","abcd"]`
- Output: `4`

**Example 3**

- Input: `words = ["a","aa","aaa","aaaa"]`
- Output: `0`
