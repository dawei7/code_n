# Reverse Words in a String III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 557 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-iii/) |

## Problem Description
### Goal
Given a string containing at least one word, with words separated by exactly one space, reverse the character sequence inside each individual word. Keep the words in their original left-to-right order.

Return the transformed string with the single spaces between words unchanged. Characters cannot move from one word to another, and reversing one word has no effect on its neighbors. A one-character word remains unchanged; the task reverses word contents rather than reversing the word order or the complete string.

### Function Contract
**Inputs**

- `s`: a string of words separated by single spaces, with no leading or trailing space

**Return value**

- A string with each word reversed in place

### Examples
**Example 1**

- Input: `s = "Let's take LeetCode contest"`
- Output: `"s'teL ekat edoCteeL tsetnoc"`

**Example 2**

- Input: `s = "Mr Ding"`
- Output: `"rM gniD"`

**Example 3**

- Input: `s = "a"`
- Output: `"a"`
