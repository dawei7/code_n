# Minimum Score of a Path Between Two Cities

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2492 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/) |

## Problem Description

### Goal

There are `n` cities numbered from $1$ through $n$. Each entry `[a, b, distance]` in `roads` describes a bidirectional road of the given positive distance between two distinct cities. The overall graph may contain components unrelated to cities $1$ and $n$.

The score of a path is the smallest road distance used anywhere along that path. Find the minimum score achievable by a path from city $1$ to city $n$. A path may revisit cities and may traverse the same road multiple times. At least one route between the two designated cities is guaranteed to exist.

### Function Contract

**Inputs**

- `n`: The number of cities, labeled from `1` to `n`.
- `roads`: Distinct undirected roads represented as `[city_a, city_b, distance]`.

The constraints satisfy $2 \le n \le 10^5$, $1 \le \lvert\texttt{roads}\rvert \le 10^5$, and each distance is between $1$ and $10^4$.

**Return value**

Return the minimum possible value of the least-distance road used by any path from city `1` to city `n`.

### Examples

#### Example 1

- **Input:** `n = 4, roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]`
- **Output:** `5`
- **Explanation:** The route `1 -> 2 -> 4` uses roads of lengths `9` and `5`, so its score is `5`, the minimum achievable value.

#### Example 2

- **Input:** `n = 4, roads = [[1, 2, 2], [1, 3, 4], [3, 4, 7]]`
- **Output:** `2`
- **Explanation:** Repetition permits `1 -> 2 -> 1 -> 3 -> 4`, which includes the length-`2` road before reaching city `4`.
