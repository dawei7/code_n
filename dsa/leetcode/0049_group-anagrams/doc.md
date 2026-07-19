# Group Anagrams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 49 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/group-anagrams/) |

## Problem Description
### Goal
You are given a list of strings containing lowercase English letters. Two strings are anagrams when one can be formed by rearranging all characters of the other, including the same multiplicity of every letter.

Partition the input occurrences into complete anagram groups and return those groups in any order. Every list entry must appear exactly once, including repeated identical strings, which remain repeated members of one group. Member order within a group may also vary. Empty strings are anagrams of one another and form their own group.

### Function Contract
**Inputs**

- `strs`: `List[str]` containing lowercase English letters

**Return value**

A `List[List[str]]` in which each inner list is one complete anagram group.

### Examples
**Example 1**

- Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[ ["eat", "tea", "ate"], ["tan", "nat"], ["bat"] ]` in any ordering

**Example 2**

- Input: `strs = [""]`
- Output: `[[""]]`

**Example 3**

- Input: `strs = ["a", "a"]`
- Output: `[["a", "a"]]`
