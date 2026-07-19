# Find the City With the Smallest Number of Neighbors at a Threshold Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1334 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Graph Theory, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) |

## Problem Description
### Goal
There are $n$ cities numbered from 0 through $n-1$. The array `edges` describes an undirected weighted graph: each record `[from, to, weight]` connects two different cities in both directions with the given positive distance. Every unordered city pair appears at most once.

For each city, count how many other cities can be reached by a path whose total distance is at most `distanceThreshold`. Return the city with the smallest such count. If several cities share that minimum, return the one with the greatest numeric index.

### Function Contract
**Inputs**

- `n`: the number of cities, where $2\le n\le100$.
- `edges`: between 1 and $n(n-1)/2$ distinct undirected edges `[from, to, weight]`, with $0\le\texttt{from}<\texttt{to}<n$ and $1\le\texttt{weight}\le10^4$.
- `distance_threshold`: the inclusive maximum path distance, between 1 and $10^4$.

**Return value**

The greatest-indexed city among those having the fewest other cities reachable within the threshold.

### Examples
**Example 1**

- Input: `n = 4`, `edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]`, `distance_threshold = 4`
- Output: `3`

**Example 2**

- Input: `n = 5`, `edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]`, `distance_threshold = 2`
- Output: `0`

**Example 3**

- Input: `n = 3`, `edges = [[0,1,5],[1,2,5],[0,2,20]]`, `distance_threshold = 10`
- Output: `2`
- Explanation: Every city can reach both others, so the greatest index wins the tie.
