# Reverse Words in a String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 186 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-ii/) |

## Problem Description
### Goal
Given a mutable array of characters containing words separated by exactly one space, reverse the order of the words. The input has no leading or trailing spaces, and each word is a contiguous sequence of non-space characters.

Modify the supplied character array in place so the last original word becomes first and the first becomes last, while every word's internal spelling remains unchanged. Keep exactly one separator between adjacent words and preserve the array's total length. Return nothing and do not allocate another character array to hold the rearranged result. An input containing one word remains unchanged.

### Function Contract
**Inputs**

- `s`: a character list containing words separated by single spaces, with no leading or trailing space

**Return value**

Return nothing. Mutate `s` in place so its words appear in reverse order while every word's spelling remains unchanged.

### Examples
**Example 1**

- Input: characters of `"the sky is blue"`
- Mutated value: characters of `"blue is sky the"`

**Example 2**

- Input: `['a']`
- Mutated value: `['a']`

**Example 3**

- Input: characters of `"hello world"`
- Mutated value: characters of `"world hello"`
