# Check if All A's Appears Before All B's

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2124 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/) |

## Problem Description
### Goal

You are given a nonempty string `s` containing only the characters `a` and
`b`. Determine whether every occurrence of `a` lies at a smaller index than
every occurrence of `b`.

Equivalently, the string must consist of one possibly empty block of `a`
characters followed by one possibly empty block of `b` characters. A string
containing only one of the two characters satisfies the condition
vacuously. Return false as soon as the ordering switches back to `a` after any
`b` has appeared; otherwise return true.

### Function Contract
**Inputs**

- `s`: A nonempty string containing only `a` and `b`. Let
  $n=\lvert s\rvert$.

**Return value**

Return `true` if every `a` occurs before every `b`; otherwise return `false`.

### Examples
**Example 1**

- Input: `s = "aaabbb"`
- Output: `true`

All three `a` characters precede all three `b` characters.

**Example 2**

- Input: `s = "abab"`
- Output: `false`

The `a` at index two occurs after the `b` at index one.

**Example 3**

- Input: `s = "bbb"`
- Output: `true`

There are no `a` characters that could violate the condition.
