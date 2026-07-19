# Expressive Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 809 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/expressive-words/) |

## Problem Description

### Goal

A word is stretchy relative to target string `s` when it can be made equal to `s` by repeatedly extending groups of identical consecutive characters. One extension adds copies of a group's character so that the resulting group has length at least `3`.

Given candidate array `words`, return how many entries are stretchy. Character-group order must match `s`; a candidate group may remain unchanged, or it may be lengthened only when the corresponding target group is at least three characters long. Characters cannot be deleted, replaced, or moved between groups.

### Function Contract

**Inputs**

- `s`: the nonempty lowercase target string.
- `words`: a list of nonempty lowercase candidate words.

**Return value**

- The number of candidates that can be stretched into `s` under the group-expansion rule.

### Examples

**Example 1**

- Input: `s = "heeellooo", words = ["hello","hi","helo"]`
- Output: `1`
- Explanation: `hello` can expand its `e` and `o` groups, while the other candidates have incompatible character groups.

**Example 2**

- Input: `s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]`
- Output: `3`
- Explanation: Both target runs have length five, so every shorter positive run of the matching character can expand to it.

**Example 3**

- Input: `s = "abcd", words = ["abc"]`
- Output: `0`
- Explanation: Stretching cannot introduce the missing `d` group.
