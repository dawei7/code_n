# Edit Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 72 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/edit-distance/) |

## Problem Description
### Goal
You are given a source string `word1` and a target string `word2`. One operation may insert a character, delete a character, or replace one character with another, and every operation has cost one.

Return the minimum total operations needed to transform the complete source into the complete target. Characters already aligned and equal require no operation. Either string may be empty, in which case every character of the other must be inserted or deleted.

### Function Contract
**Inputs**

- `word1`: the source string
- `word2`: the target string

**Return value**

The minimum edit count as an integer.

### Examples
**Example 1**

- Input: `word1 = "horse", word2 = "ros"`
- Output: `3`

**Example 2**

- Input: `word1 = "intention", word2 = "execution"`
- Output: `5`

**Example 3**

- Input: `word1 = "", word2 = "abc"`
- Output: `3`
