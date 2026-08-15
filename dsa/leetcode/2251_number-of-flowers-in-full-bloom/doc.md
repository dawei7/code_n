# Number of Flowers in Full Bloom

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2251 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) |

## Problem Description

### Goal

Each pair `[start, end]` in `flowers` gives the inclusive interval during
which one flower is in full bloom. Each value in `people` is the arrival time
of one person.

For every arrival, count how many bloom intervals contain that time. Return
the counts in the same order as `people`; repeated arrival times therefore
produce repeated answers. Each flower contributes independently whenever its
own inclusive interval covers the arrival.

### Function Contract

**Inputs**

- `flowers`: Between $1$ and $5\cdot10^4$ inclusive intervals `[start, end]`, where $1\le\texttt{start}\le\texttt{end}\le10^9$.
- `people`: Between $1$ and $5\cdot10^4$ arrival times, each between $1$ and $10^9$.

**Return value**

Return one count per arrival time, preserving input order, equal to the number
of intervals satisfying $\texttt{start}\le\texttt{time}\le\texttt{end}$.

### Examples

#### Example 1

- **Input:** `flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]`
- **Output:** `[1,2,2,2]`

#### Example 2

- **Input:** `flowers = [[1,10],[3,3]], people = [3,3,2]`
- **Output:** `[2,2,1]`

#### Example 3

- **Input:** `flowers = [[5,5]], people = [4,5,6]`
- **Output:** `[0,1,0]`
