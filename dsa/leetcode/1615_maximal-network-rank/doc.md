# Maximal Network Rank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1615 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximal-network-rank/) |

## Problem Description
### Goal
An infrastructure contains `n` cities numbered from 0 through `n - 1`. Every entry `[a, b]` in `roads` represents one bidirectional road directly connecting cities `a` and `b`; no city connects to itself, and no pair has more than one road.

For two different cities, their network rank is the number of distinct roads directly connected to at least one of them. A road joining the selected cities touches both, but contributes only once. Return the maximal network rank among all pairs of different cities. The overall graph does not need to be connected.

### Function Contract
**Inputs**

- `n`: the number of cities, with $2 \le n \le 100$.
- `roads`: a list of $m$ distinct undirected edges `[a, b]`, where $0 \le a,b < n$ and $a \ne b$.
- At most one road connects any unordered pair, so $0 \le m \le n(n-1)/2$.

**Return value**

Return the greatest number of distinct roads incident to either city in any pair of different cities.

### Examples
**Example 1**

- Input: `n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]`
- Output: `4`

**Example 2**

- Input: `n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]`
- Output: `5`

**Example 3**

- Input: `n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]`
- Output: `5`
