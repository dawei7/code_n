# Equalize Strings by Adding or Removing Characters at Ends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3135 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Binary Search, Dynamic Programming, Sliding Window, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/) |

## Problem Description

### Goal

You are given two strings, `initial` and `target`. Modify `initial` until it equals `target` by applying a sequence of permitted operations.

In one operation, add one lowercase English letter to the beginning or end of `initial`, or remove one character from its beginning or end. Characters cannot be inserted into or removed from an interior position.

Return the minimum number of operations needed to transform `initial` into `target`.

### Function Contract

Let $m = \lvert\texttt{initial}\rvert$ and $n = \lvert\texttt{target}\rvert$.

**Inputs**

- `initial`: The starting string, with $1 \le m \le 1000$.
- `target`: The required final string, with $1 \le n \le 1000$.

Both strings consist only of lowercase English letters.

**Return value**

- Return the minimum number of allowed end operations required to make `initial` equal `target`.

### Examples

#### Example 1

- **Input:** `initial = "abcde", target = "cdef"`
- **Output:** `3`
- **Explanation:** Remove `'a'` and `'b'` from the beginning, then add `'f'` to the end.

#### Example 2

- **Input:** `initial = "axxy", target = "yabx"`
- **Output:** `6`
- **Explanation:** One optimal sequence adds `'y'` at the beginning, removes three characters from the end, and appends `'b'` and `'x'`.

#### Example 3

- **Input:** `initial = "xyz", target = "xyz"`
- **Output:** `0`
- **Explanation:** The strings already match, so no operation is necessary.
