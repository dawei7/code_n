# Maximum Score From Removing Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1717 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-from-removing-substrings/) |

## Problem Description

### Goal

You are given a lowercase English string `s` and two positive scores, `x` and `y`. At any time, you may delete an adjacent occurrence of `ab` and add `x` points, or delete an adjacent occurrence of `ba` and add `y` points. A deletion joins the characters on its two sides, so it can create another removable pair.

Choose both the order and locations of the deletions. Return the greatest total score obtainable after performing either operation any number of times; characters other than `a` and `b` cannot be removed and therefore separate the string into independent regions.

### Function Contract

**Inputs**

- `s`: a string of lowercase English letters, with $1 \le \lvert \texttt{s} \rvert \le 10^5$.
- `x`: the points gained for removing `ab`, with $1 \le x \le 10^4$.
- `y`: the points gained for removing `ba`, with $1 \le y \le 10^4$.

**Return value**

- Return the maximum total points obtainable by repeatedly removing `ab` and `ba`.

### Examples

**Example 1**

- Input: `s = "cdbcbbaaabab", x = 4, y = 5`
- Output: `19`
- Explanation: Removing three `ba` pairs and one `ab` pair yields $3 \cdot 5 + 4 = 19$ points.

**Example 2**

- Input: `s = "aabbaaxybbaabb", x = 5, y = 4`
- Output: `20`
- Explanation: The characters `x` and `y` separate independent `a`/`b` regions; four profitable removals are available in total.

**Example 3**

- Input: `s = "abba", x = 10, y = 1`
- Output: `11`
- Explanation: Delete the higher-valued `ab` first, leaving `ba`; both pairs can then be scored.
