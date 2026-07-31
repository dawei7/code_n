# Lexicographically Smallest Generated String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3474 |
| Difficulty | Hard |
| Topics | String, Greedy, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/lexicographically-smallest-generated-string/) |

## Problem Description
### Goal
You are given a condition string `str1` of length $n$ containing only `'T'` and `'F'`, and a lowercase pattern `str2` of length $m$. Construct a lowercase string `word` of length $n+m-1$. For every index $i$ from $0$ through $n-1$, compare `str2` with the length-$m$ substring `word[i:i + m]`.

If `str1[i]` is `'T'`, that substring must equal `str2` exactly. If `str1[i]` is `'F'`, it must not equal `str2`. All conditions apply simultaneously, including conditions whose windows overlap. Return the lexicographically smallest `word` satisfying every condition, or return `""` when overlapping requirements make construction impossible.

### Function Contract
**Inputs**

- `str1`: The `'T'`/`'F'` condition for each possible pattern-length window.
- `str2`: The lowercase pattern that each window must equal or avoid.

Let $n=\lvert\texttt{str1}\rvert$ and $m=\lvert\texttt{str2}\rvert$. The constraints are $1\le n\le10^4$ and $1\le m\le500$.

**Return value**

Return the lexicographically smallest valid generated string of length $n+m-1$, or `""` if none exists.

### Examples
**Example 1**

- Input: `str1 = "TFTF", str2 = "ab"`
- Output: `"ababa"`

The windows beginning at indices `0` and `2` equal `"ab"`, while those beginning at `1` and `3` do not.

**Example 2**

- Input: `str1 = "TFTF", str2 = "abc"`
- Output: `""`

The overlapping true windows impose inconsistent characters, so no generated string exists.

**Example 3**

- Input: `str1 = "F", str2 = "d"`
- Output: `"a"`

The lexicographically smallest one-character string already differs from the pattern.
