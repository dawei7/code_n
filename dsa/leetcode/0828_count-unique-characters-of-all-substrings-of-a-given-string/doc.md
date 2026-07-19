# Count Unique Characters of All Substrings of a Given String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 828 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/) |

## Problem Description

### Goal

For any string `t`, define `countUniqueChars(t)` as the number of characters that occur exactly once in `t`. For example, `countUniqueChars("LEETCODE")` is `5` because `L`, `T`, `C`, `O`, and `D` each appear once, while `E` appears three times.

Given an uppercase English string `s`, consider every nonempty substring selected by a pair of start and end positions. Return the sum of `countUniqueChars(t)` over all those substrings. Equal substring values arising at different positions are separate substrings and must each contribute. The input guarantees that the final sum fits in a 32-bit integer.

### Function Contract

**Inputs**

- `s`: a string of $n$ uppercase English letters, where $1 \le n \le 10^5$
- Let $A=26$ be the alphabet size.

**Return value**

- The sum, over every nonempty positional substring of `s`, of the number of characters occurring exactly once in that substring

### Examples

**Example 1**

- Input: `s = "ABC"`
- Output: `10`
- Explanation: Every character in every substring is unique, so the six substrings contribute `1 + 1 + 1 + 2 + 2 + 3`.

**Example 2**

- Input: `s = "ABA"`
- Output: `8`
- Explanation: The complete substring has only `B` as a unique character, while the shorter positional substrings contribute the remaining `7`.

**Example 3**

- Input: `s = "LEETCODE"`
- Output: `92`
