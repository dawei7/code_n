# Count Pairs That Form a Complete Day I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3184 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/) |

## Problem Description

### Goal

The integer array `hours` contains time durations measured in hours. Count the pairs of indices $(i,j)$ with $i<j$ whose two durations combine to form a complete number of days.

A complete day is exactly 24 hours, so a pair qualifies when its sum is an exact multiple of 24. The multiple may represent one day, two days, three days, or any larger whole number of days.

Return the number of qualifying index pairs.

### Function Contract

**Inputs**

- `hours`: A list of $n$ positive hour durations, where $1\le n\le100$ and $1\le\texttt{hours[i]}\le10^9$.

**Return value**

- The number of index pairs $(i,j)$ satisfying $i<j$ and $(\texttt{hours[i]}+\texttt{hours[j]})\bmod24=0$.

### Examples

**Example 1**

- Input: `hours = [12, 12, 30, 24, 24]`
- Output: `2`

Indices $(0,1)$ sum to 24 hours, and indices $(3,4)$ sum to 48 hours.

**Example 2**

- Input: `hours = [72, 48, 24, 3]`
- Output: `3`

The three durations divisible by 24 form the qualifying pairs $(0,1)$, $(0,2)$, and $(1,2)$.
