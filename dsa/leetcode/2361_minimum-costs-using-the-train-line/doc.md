# Minimum Costs Using the Train Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2361 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-costs-using-the-train-line/) |

## Problem Description

### Goal

A city train line has regular and express routes passing through the same
$n+1$ stops, numbered from 0 through $n$. You begin on the regular route at
stop 0. For each segment from stop $i-1$ to stop $i$, `regular[i]` and
`express[i]` give the respective travel costs.

Moving from regular to express costs `expressCost` every time that transfer is
made. Returning from express to regular is free, and remaining on the express
route has no additional transfer cost. Return the minimum total cost to reach
each stop 1 through $n$ from stop 0; reaching a stop on either route counts.

### Function Contract

**Inputs**

- `regular`: The $n$ positive costs of consecutive regular-route segments.
- `express`: The $n$ positive costs of consecutive express-route segments.
- `expressCost`: The positive cost paid on each regular-to-express transfer.

The arrays have equal length $1 \le n \le 10^5$, and every cost is between
1 and $10^5$ inclusive.

**Return value**

Return a length-$n$ list whose entry at index $i-1$ is the minimum cost to
reach stop $i$ on either route. Totals may require 64-bit integers.

### Examples

**Example 1**

- Input: `regular = [1,6,9,5], express = [5,2,3,10], expressCost = 8`
- Output: `[1,7,14,19]`

**Example 2**

- Input: `regular = [11,5,13], express = [7,10,6], expressCost = 3`
- Output: `[10,15,24]`
