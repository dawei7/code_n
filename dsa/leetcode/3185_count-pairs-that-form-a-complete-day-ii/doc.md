# Count Pairs That Form a Complete Day II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3185 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/) |

## Problem Description

### Goal

The integer array `hours` contains time durations measured in hours. Count the pairs of indices $(i,j)$ with $i<j$ whose two durations together represent a complete number of days.

One complete day lasts exactly 24 hours. Therefore, a pair qualifies when the sum of its durations is an exact multiple of 24, whether that multiple represents one day, two days, three days, or more.

Return the total number of qualifying index pairs. The array may contain as many as $5\cdot10^5$ durations, so the result and the method must handle a large number of possible pairs.

### Function Contract

**Inputs**

- `hours`: A list of $n$ positive hour durations, where $1\le n\le5\cdot10^5$ and $1\le\texttt{hours[i]}\le10^9$.

**Return value**

- The number of index pairs $(i,j)$ satisfying $i<j$ and $(\texttt{hours[i]}+\texttt{hours[j]})\bmod24=0$.

### Examples

#### Example 1

- **Input:** `hours = [12, 12, 30, 24, 24]`
- **Output:** `2`

Indices $(0,1)$ sum to 24 hours, while indices $(3,4)$ sum to 48 hours.

#### Example 2

- **Input:** `hours = [72, 48, 24, 3]`
- **Output:** `3`

The three durations divisible by 24 form the qualifying pairs $(0,1)$, $(0,2)$, and $(1,2)$.
