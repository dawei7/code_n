# Check Distances Between Same Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2399 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-distances-between-same-letters/) |

## Problem Description

### Goal

You are given a 0-indexed lowercase string `s` in which every letter that
appears occurs exactly twice. You also receive a 26-element array `distance`;
index 0 corresponds to `a`, index 1 to `b`, and so on through `z`.

The string is well-spaced when, for every letter present in `s`, the number of
string positions strictly between its two occurrences equals that letter's
entry in `distance`. Entries belonging to letters absent from `s` have no
effect and must be ignored. Return whether all present letters satisfy their
individual requirements.

### Function Contract

**Inputs**

- `s`: A lowercase string of length $n$, where $2 \le n \le 52$ and every
  present letter occurs exactly twice.
- `distance`: A list of exactly 26 integers, each between 0 and 50 inclusive.

**Return value**

Return `True` if, for every letter at alphabet index $c$ with occurrence
positions $p_c<q_c$, the equality
$q_c-p_c-1=\texttt{distance[c]}$ holds. Return `False` if any present letter
violates it.

### Examples

#### Example 1

- **Input:** `s = "abaccb"`,
  `distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]`
- **Output:** `True`
- **Explanation:** The two `a`, `b`, and `c` occurrences have respectively 1, 3,
  and 0 characters between them. The value for absent `d` is ignored.

#### Example 2

- **Input:** `s = "aa"`,
  `distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]`
- **Output:** `False`
- **Explanation:** Adjacent occurrences have distance zero, not one.

#### Example 3

- **Input:** `s = "aa"`,
  `distance = [0,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]`
- **Output:** `True`
- **Explanation:** Only `a` appears, so every other entry is irrelevant.
