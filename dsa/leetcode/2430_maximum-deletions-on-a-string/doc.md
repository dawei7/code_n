# Maximum Deletions on a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2430 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Deletions on a String](https://leetcode.com/problems/maximum-deletions-on-a-string/) |

## Problem Description

### Goal

You are given a string `s` containing only lowercase English letters. An operation may always delete the entire current string. Alternatively, choose an integer $i$ with $1 \le i \le \lfloor \lvert s\rvert/2\rfloor$ and delete the first $i$ characters, but only when that prefix is exactly equal to the $i$ characters immediately following it.

Each operation changes the current string, so the next comparison starts at its new beginning. Delete all characters while maximizing the total number of operations, and return that maximum. Equal text appearing later is not sufficient: the two compared blocks must be adjacent at the current prefix.

### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

Its length $n$ satisfies $1 \le n \le 4000$.

**Return value**

- The maximum number of valid operations that can delete all of `s`.

### Examples

**Example 1**

- Input: `s = "abcabcdabc"`
- Output: `2`

Delete the first `"abc"` because the next three characters match it, leaving `"abcdabc"`, and then delete the entire remainder.

**Example 2**

- Input: `s = "aaabaab"`
- Output: `4`

One optimal sequence removes `"a"`, then `"aab"`, then `"a"`, and finally deletes the remaining `"ab"`.

**Example 3**

- Input: `s = "aaaaa"`
- Output: `5`

Each operation can remove one character because the first two remaining characters are equal until only one remains.
