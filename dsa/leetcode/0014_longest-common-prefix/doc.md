# Longest Common Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 14 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-common-prefix/) |

## Problem Description
### Goal
Given a nonempty array of strings `strs`, find the longest sequence of characters that begins every string in the array. A prefix must start at position zero; matching characters that occur later in a string do not count.

Return the shared prefix itself. Its length cannot exceed that of the shortest input string, and a one-element array has that entire string as its common prefix. If the strings disagree at their first character, or one input is empty, return the empty string.

### Function Contract
**Inputs**

- `strs`: non-empty `List[str]`

**Return value**

A `str` containing the longest common prefix.

### Examples
**Example 1**

- Input: `strs = ["flower", "flow", "flight"]`
- Output: `"fl"`

**Example 2**

- Input: `strs = ["dog", "racecar", "car"]`
- Output: `""`

**Example 3**

- Input: `strs = ["alone"]`
- Output: `"alone"`
