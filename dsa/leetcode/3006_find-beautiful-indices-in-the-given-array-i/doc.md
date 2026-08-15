# Find Beautiful Indices in the Given Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3006 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Binary Search, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/) |

## Problem Description

### Goal

You are given a 0-indexed lowercase string `s`, two nonempty lowercase
patterns `a` and `b`, and an integer `k`.

An index `i` is beautiful when `a` starts at `i` in `s` and some
occurrence of `b` starts at an index `j` satisfying
$\lvert j-i\rvert\le k$. Both occurrences must fit fully inside `s`.

Return every beautiful index in increasing order.

### Function Contract

**Inputs**

- `s`: the text string
- `a`: the pattern whose qualifying start indices are returned
- `b`: the pattern that must occur nearby
- `k`: the inclusive maximum distance between occurrence starts

Let $N=\lvert\texttt{s}\rvert$. The contract guarantees
$1\le k\le N\le10^5$, $1\le\lvert\texttt{a}\rvert,
\lvert\texttt{b}\rvert\le10$, and lowercase English letters only.

**Return value**

Return the sorted list of all indices where `a` occurs within distance `k`
of at least one occurrence of `b`.

### Examples

#### Example 1

- **Input:** `s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15`
- **Output:** `[16,33]`

The `"my"` occurrences at 16 and 33 are respectively within 15 positions of
`"squirrel"` occurrences at 4 and 18.

#### Example 2

- **Input:** `s = "abcd", a = "a", b = "a", k = 4`
- **Output:** `[0]`

The occurrence at index 0 can serve as both pattern occurrences.
