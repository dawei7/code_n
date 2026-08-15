# Minimum Difference in Sums After Removal of Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2163 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/) |

## Problem Description

### Goal

Let `nums` contain exactly $3n$ positive integers. Remove a subsequence of
exactly $n$ elements, preserving the relative order of all values that remain.
The resulting sequence has $2n$ elements and is divided by position into two
equal parts: its first $n$ values and its final $n$ values.

Let the sums of those parts be $S_{\mathrm{first}}$ and
$S_{\mathrm{second}}$. The result of a removal is the signed difference
$S_{\mathrm{first}}-S_{\mathrm{second}}$, which may be negative. Return the
smallest difference attainable over every valid choice of removed subsequence.

### Function Contract

**Inputs**

- `nums`: an array of $3n$ integers, where $1\le n\le 10^5$ and every value is
  between $1$ and $10^5$.

Removing a subsequence does not reorder the retained elements.

**Return value**

Return the minimum possible value of
$S_{\mathrm{first}}-S_{\mathrm{second}}$ after exactly $n$ removals.

### Examples

#### Example 1

- **Input:** `nums = [3, 1, 2]`
- **Output:** `-1`

Removing `3` leaves `[1, 2]`, whose two one-element part sums differ by
$1-2=-1$.

#### Example 2

- **Input:** `nums = [7, 9, 5, 8, 1, 3]`
- **Output:** `1`

Removing `9` and `1` leaves `[7, 5, 8, 3]`; the difference is
$(7+5)-(8+3)=1$.

#### Example 3

- **Input:** `nums = [1, 2, 3, 4, 5, 6]`
- **Output:** `-8`

One optimal removal leaves `[1, 2, 5, 6]`, producing
$(1+2)-(5+6)=-8$.
