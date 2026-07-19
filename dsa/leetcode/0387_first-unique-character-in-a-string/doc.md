# First Unique Character in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 387 |
| Difficulty | Easy |
| Topics | Hash Table, String, Queue, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/) |

## Problem Description
### Goal
Given a string of lowercase English letters, find the earliest character occurrence whose total frequency across the entire string is exactly one. A character cannot qualify merely because it has not appeared earlier if another occurrence appears later.

Return the zero-based index of the first unique character. If every character repeats, return `-1`. Repeated characters may be separated by many positions and still disqualify one another. The task returns an index rather than the character itself, and among several unique characters only the leftmost position is accepted.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters

**Return value**

- Return the zero-based index of the first character with total frequency one, or `-1` when no such character exists.

### Examples
**Example 1**

- Input: `s = "leetcode"`
- Output: `0`

**Example 2**

- Input: `s = "loveleetcode"`
- Output: `2`

**Example 3**

- Input: `s = "aabb"`
- Output: `-1`
