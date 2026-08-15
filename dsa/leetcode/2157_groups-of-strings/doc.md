# Groups of Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2157 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/groups-of-strings/) |

## Problem Description

### Goal

You are given an array `words` of lowercase English strings. Within each word,
every letter occurs at most once. Treat a word as its set of letters. Two
strings are directly connected when one letter set can be changed into the
other by exactly one operation: add one letter, delete one letter, or replace
one letter with any letter, including the same letter.

Partition all strings into non-overlapping groups so that no string in one
group is connected, directly or through other group members, to a string in a
different group. A string with no connection forms a group by itself. Return
the maximum possible number of groups together with the number of strings in
the largest group; this grouping is uniquely determined.

### Function Contract

**Inputs**

- `words`: an array of $n$ strings, where $1 \le n \le 2\cdot10^4$. Each word
  has length from $1$ through $26$, uses only lowercase English letters, and
  contains no repeated letter.

**Return value**

A two-element list `[group_count, largest_group_size]`.

### Examples

#### Example 1

- **Input:** `words = ["a", "b", "ab", "cde"]`
- **Output:** `[2, 3]`
- **Explanation:** `"a"`, `"b"`, and `"ab"` are connected by replacement and
  addition/deletion operations, while `"cde"` is isolated.

#### Example 2

- **Input:** `words = ["a", "ab", "abc"]`
- **Output:** `[1, 3]`
- **Explanation:** Consecutive words differ by adding one letter, so all three
  belong to one group.
