# Count the Number of Special Characters I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3120 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-i/) |

## Problem Description

### Goal

You are given a string `word` made only of lowercase and uppercase English letters. A letter is special when both of its cases occur somewhere in `word`: for example, `a` contributes when the string contains at least one `a` and at least one `A`.

Return the number of distinct special letters. Occurrence order does not matter, and repeated appearances of either case do not increase the count; each underlying English letter contributes either one or zero.

### Function Contract

**Inputs**

- `word`: A string of lowercase and uppercase English letters.

Its length $n$ satisfies $1 \le n \le 50$.

**Return value**

Return the number of distinct letters whose lowercase and uppercase forms both appear in `word`.

### Examples

#### Example 1

- **Input:** `word = "aaAbcBC"`
- **Output:** `3`
- **Explanation:** The letters `a`, `b`, and `c` each occur in both cases.

#### Example 2

- **Input:** `word = "abc"`
- **Output:** `0`
- **Explanation:** No uppercase form appears for any letter in the string.

#### Example 3

- **Input:** `word = "abBCab"`
- **Output:** `1`
- **Explanation:** Only `b` occurs in both lowercase and uppercase.
