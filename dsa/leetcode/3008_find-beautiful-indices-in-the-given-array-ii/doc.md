# Find Beautiful Indices in the Given Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3008 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Binary Search, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/) |

## Problem Description
### Goal
You are given a 0-indexed lowercase text `s`, lowercase patterns `a` and
`b`, and an integer `k`.

An index `i` is beautiful when `a` occurs in `s` starting at `i` and
there is an occurrence of `b` starting at some index `j` with
$\lvert j-i\rvert\le k$. Both pattern occurrences must lie fully inside the
text.

Return every beautiful index in increasing order.

### Function Contract
**Inputs**

- `s`: the text searched for both patterns
- `a`: the pattern whose qualifying start indices are returned
- `b`: the pattern required within the distance limit
- `k`: the inclusive maximum difference between start indices

Let $N=\lvert\texttt{s}\rvert$, $A=\lvert\texttt{a}\rvert$, and
$B=\lvert\texttt{b}\rvert$. The contract guarantees
$1\le k\le N\le5\cdot10^5$, $1\le A,B\le5\cdot10^5$, and lowercase
English letters only.

**Return value**

Return the sorted list of all qualifying starts of `a`.

### Examples
**Example 1**

- Input: `s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15`
- Output: `[16,33]`

The starts 16 and 33 have `"squirrel"` starts at 4 and 18 within the allowed
distance.

**Example 2**

- Input: `s = "abcd", a = "a", b = "a", k = 4`
- Output: `[0]`

The occurrence at 0 witnesses both patterns and has distance zero.
