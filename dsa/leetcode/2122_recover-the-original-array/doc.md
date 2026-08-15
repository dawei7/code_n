# Recover the Original Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2122 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Enumeration, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/recover-the-original-array/) |

## Problem Description

### Goal

An unknown zero-indexed array `arr` contains $n$ positive integers. A positive
integer $k$ was chosen, and each original value produced two numbers:
`arr[i] - k` in an array `lower` and `arr[i] + k` in an array `higher`.

The two derived arrays were then combined and shuffled, so `nums` contains all
$2n$ derived values without identifying which copy came from `lower` or
`higher`. Duplicate values retain their full multiplicity, including cases
where a lower value from one element equals a higher value from another.

Recover any positive array `arr` for which one shared positive integer $k$
reproduces exactly the multiset in `nums`. At least one valid recovery is
guaranteed, and different valid answers may exist.

### Function Contract

**Inputs**

- `nums`: A list of $2n$ positive integers formed by shuffling the complete
  `lower` and `higher` arrays.

**Return value**

Return any list of $n$ positive integers for which there is an integer $k>0$
such that

$$
\{\!\{a-k:a\in\texttt{arr}\}\!\}
\uplus
\{\!\{a+k:a\in\texttt{arr}\}\!\}
=
\{\!\{\texttt{nums}\}\!\}.
$$

The equality is multiset equality, so duplicate counts must match.

### Examples

#### Example 1

- **Input:** `nums = [2, 10, 6, 4, 8, 12]`
- **Output:** `[3, 7, 11]`

With $k=1$, this yields lower values `[2, 6, 10]` and higher values
`[4, 8, 12]`. The alternative `[5, 7, 9]` with $k=3$ is also valid.

#### Example 2

- **Input:** `nums = [1, 1, 3, 3]`
- **Output:** `[2, 2]`

Here $k=1$ and both original values are equal.

#### Example 3

- **Input:** `nums = [5, 435]`
- **Output:** `[220]`

The only pair has midpoint $220$ and half-difference $215$.
