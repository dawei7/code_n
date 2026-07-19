# Partition Labels

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 763 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-labels/) |

## Problem Description

### Goal

Given a string `s`, partition it into as many nonempty consecutive parts as possible so that each distinct letter appears in at most one part. Every character must belong to exactly one part, and the parts must preserve the string's original order.

Return a list containing the part lengths from left to right. A letter may occur several times inside its one assigned part, but no occurrence of that letter may appear in another part; maximizing the number of parts determines where valid cuts should be made.

### Function Contract

**Inputs**

- `s`: a nonempty lowercase string.

**Return value**

- A list of positive partition lengths whose sum is `len(s)` and whose partitions do not share any letter.

### Examples

**Example 1**

- Input: `s = "ababcbacadefegdehijhklij"`
- Output: `[9,7,8]`
- Explanation: Each letter is confined to one of the three parts, and no valid partition can end earlier.

**Example 2**

- Input: `s = "eccbbbbdec"`
- Output: `[10]`
- Explanation: Occurrences link every position into one required partition.

**Example 3**

- Input: `s = "ynbi"`
- Output: `[1,1,1,1]`
- Explanation: Every character is unique, so every position can be its own part.
