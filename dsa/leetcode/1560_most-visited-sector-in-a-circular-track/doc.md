# Most Visited Sector in a Circular Track

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1560 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/most-visited-sector-in-a-circular-track/) |

## Problem Description
### Goal

A circular track contains `n` sectors labeled from `1` through `n`. Movement follows increasing labels, wrapping from sector `n` back to sector `1`. A marathon consists of $m$ rounds: round $i$ starts at `rounds[i - 1]` and finishes at `rounds[i]`.

Count a sector whenever the runner visits it, including the initial sector and every round endpoint. Return all sectors tied for the greatest visit count, sorted in ascending numeric order.

### Function Contract
**Inputs**

- `n`: The number of sectors, where $2 \le n \le 100$.
- `rounds`: A list of $m+1$ checkpoints, where $1 \le m \le 100$ and every checkpoint lies in $[1,n]$.
- Consecutive checkpoints are distinct, and travel between them always follows increasing sector labels with wraparound.

**Return value**

Return the most frequently visited sector labels in strictly increasing order.

### Examples
**Example 1**

- Input: `n = 4, rounds = [1,3,1,2]`
- Output: `[1,2]`

**Example 2**

- Input: `n = 2, rounds = [2,1,2,1,2,1,2,1,2]`
- Output: `[2]`

**Example 3**

- Input: `n = 7, rounds = [1,3,5,7]`
- Output: `[1,2,3,4,5,6,7]`
