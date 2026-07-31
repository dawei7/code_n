# Properties Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3493 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/properties-graph/) |

## Problem Description

### Goal

Each row of the rectangular matrix `properties` describes one graph node. For two rows, their intersection size is the number of **distinct** integer values that appear in both rows; repeated occurrences within either row count only once. Create an undirected edge between two different row indices exactly when this intersection size is at least `k`.

After considering every pair of row indices, determine how many connected components the resulting undirected graph contains. Connectivity is transitive: two rows belong to the same component even without a direct edge when a path through other qualifying rows connects them.

### Function Contract

**Inputs**

- `properties`: An $n\times m$ integer matrix whose rows define the graph nodes.
- `k`: The minimum number of distinct shared values required to create an edge.

The dimensions satisfy $1\le n\le100$ and $1\le m\le100$. Every matrix value is between $1$ and $100$, and $1\le k\le m$.

**Return value**

Return the number of connected components in the graph defined by the qualifying row intersections.

### Examples

**Example 1**

- Input: `properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1`
- Output: `3`
- Explanation: The first two rows form one component, rows two through four by index form another through values `4` and `5`, and the final row is isolated.

**Example 2**

- Input: `properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2`
- Output: `1`
- Explanation: The first two rows share `2` and `3`, while the last two share `3` and `4`, so all three nodes are connected transitively.

**Example 3**

- Input: `properties = [[1,1],[1,1]], k = 2`
- Output: `2`
- Explanation: The only distinct common value is `1`, so the threshold is not met.
