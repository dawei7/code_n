# Maximum Points Tourist Can Earn

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3332 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-points-tourist-can-earn/) |

## Problem Description

### Goal

A tourist will spend exactly $k$ days in a country containing $n$ cities. Every city is directly connected to every other city, and the tourist may choose any city as the starting location before day $0$. The journey's days are indexed from $0$ through $k-1$.

On each day, the tourist must choose one of two actions. Staying in the current city `curr` earns `stayScore[day][curr]` points. Traveling from `curr` to a different city `dest` earns `travelScore[curr][dest]` points and makes `dest` the current city; a travel action does not also earn that day's stay score. Determine the maximum total points obtainable over all starting cities and valid sequences of exactly $k$ actions.

### Function Contract

**Inputs**

- `n`: The number of cities, where $1 \le n \le 200$.
- `k`: The exact number of days, where $1 \le k \le 200$.
- `stayScore`: A $k \times n$ integer matrix where `stayScore[day][city]` is the score for staying in `city` on `day`; every entry is between $1$ and $100$.
- `travelScore`: An $n \times n$ integer matrix where `travelScore[curr][dest]` is the score for moving from `curr` to `dest`; entries are between $0$ and $100$, and `travelScore[city][city] = 0`.

**Return value**

- The maximum total score the tourist can earn during the $k$ days.

### Examples

#### Example 1

- **Input:** `n = 2, k = 1, stayScore = [[2, 3]], travelScore = [[0, 2], [1, 0]]`
- **Output:** `3`
- **Explanation:** Start in city $1$ and stay there.

#### Example 2

- **Input:** `n = 3, k = 2, stayScore = [[3, 4, 2], [2, 1, 2]], travelScore = [[0, 2, 1], [2, 0, 4], [3, 2, 0]]`
- **Output:** `8`
- **Explanation:** Start in city $1$, stay there on day $0$, then travel to city $2$ on day $1$.
