# The Most Similar Path in a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1548 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/the-most-similar-path-in-a-graph/) |

## Problem Description
### Goal
An undirected connected graph has `n` cities numbered from zero to $n-1$. Each city has a name given by `names[city]`, and every pair in `roads` connects two cities that may be consecutive in a route.

Construct a route containing exactly as many cities as `targetPath` contains names. Consecutive route entries must be connected by a road; revisiting cities and roads is allowed. The edit distance of the route is the number of positions where the visited city's name differs from the corresponding target name. Return any valid route with minimum possible edit distance.

### Function Contract
**Inputs**

- `n`: the number of cities, where $2 \le n \le 100$.
- `roads`: $e$ distinct undirected edges joining different city indices. The graph is connected.
- `names`: exactly $n$ uppercase city names, one for each city.
- `targetPath`: a list of $m$ uppercase target names, where $1 \le m \le 100$.

**Return value**

Any list of $m$ city indices forming a graph walk whose positional name mismatch count against `targetPath` is minimum. Multiple optimal routes may be valid.

### Examples
**Example 1**

- Input: `n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]`
- Output: `[0, 2, 4, 2]`
- Explanation: The city names are `["ATL","LAX","HND","LAX"]`, differing from the target only at the second position.

**Example 2**

- Input: the same graph and names, with `targetPath = ["ATL","LAX","PEK"]`
- Output: `[0, 2, 1]`
- Explanation: Every consecutive pair is a road and all three names match, so the edit distance is zero.

**Example 3**

- Input: `n = 2, roads = [[0,1]], names = ["A","B"], targetPath = ["B","A","B"]`
- Output: `[1, 0, 1]`
- Explanation: The only alternating walk matches every target name.
