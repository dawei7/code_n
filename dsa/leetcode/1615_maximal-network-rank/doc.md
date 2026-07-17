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

### Required Complexity
- **Time:** $O(n^2+m)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Separate incident counts from shared-road detection.** Process every road once. Increment the degree of each endpoint, and mark the two cities as directly connected in a symmetric Boolean matrix. The degree array then counts every road touching each city, while the matrix answers whether a particular pair shares one road in constant time.

**Evaluate each unordered city pair once.** For cities `first < second`, adding their degrees counts all roads incident to either city. Every road other than `[first, second]` touches at most one selected endpoint and is counted once. If the selected cities are adjacent, their shared road appears in both degrees, so subtract one Boolean connection indicator. Thus `degree[first] + degree[second] - connected[first][second]` is exactly that pair's network rank.

Taking the maximum across all $n(n-1)/2$ unordered pairs considers every legal choice of two different cities. Since each pair formula counts precisely the union of its incident roads, the largest computed value is the infrastructure's maximal network rank.

#### Complexity detail

Building degrees and connections takes $O(m)$ time. Inspecting every unordered city pair takes $O(n^2)$ time, for $O(n^2+m)$ overall. The Boolean connection matrix uses $O(n^2)$ space and the degree array uses $O(n)$ more.

#### Alternatives and edge cases

- **Adjacency sets:** Store each city's neighbors in a set instead of a matrix. Membership remains expected $O(1)$ and space falls to $O(n+m)$, with the same expected time bound.
- **Rescan roads for every pair:** Building the union of incident roads separately for each city pair is correct but can require $O(n^2m)$ time.
- With no roads, every pair has rank zero.
- Isolated cities remain valid pair members, although pairing two isolated cities contributes no roads.
- If the chosen cities are directly connected, their shared road must be subtracted exactly once.
- Disconnected components do not restrict the choice; cities from different components can form the best pair.
- In a complete graph, any pair has rank $2n-3$, not $2n-2$, because its connecting road is shared.

</details>
