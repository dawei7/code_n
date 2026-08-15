# Count Connected Components in LCM Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3378 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Union-Find, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-connected-components-in-lcm-graph/) |

## Problem Description

### Goal

An array `nums` of $n$ distinct positive integers defines an undirected graph with one node for each array position. Nodes `i` and `j` share an edge exactly when the least common multiple of `nums[i]` and `nums[j]` is at most the positive integer `threshold`.

Return the number of connected components in this graph. Connectivity is transitive: two values belong to the same component when some path of qualifying LCM edges joins them, even if their own LCM is greater than `threshold`. A value greater than `threshold` cannot share an edge with any other positive value because their LCM is at least that value.

### Function Contract

**Inputs**

- `nums`: A list of $n$ distinct positive integers that label the graph nodes.
- `threshold`: The positive upper bound for an edge's least common multiple.

The constraints are $1\leq n\leq10^5$, $1\leq\texttt{nums[i]}\leq10^9$, and $1\leq\texttt{threshold}\leq2\cdot10^5$. Let $T=\texttt{threshold}$.

**Return value**

- The number of connected components in the graph induced by the LCM condition.

### Examples

#### Example 1

- **Input:** `nums = [2,4,8,3,9]`, `threshold = 5`
- **Output:** `4`
- **Explanation:** Only `2` and `4` share a qualifying edge; the other three values are isolated.

#### Example 2

- **Input:** `nums = [2,4,8,3,9,12]`, `threshold = 10`
- **Output:** `2`
- **Explanation:** The values `2`, `3`, `4`, `8`, and `9` are connected through qualifying edges, while `12` is isolated.

#### Example 3

- **Input:** `nums = [2,6,30,35]`, `threshold = 12`
- **Output:** `3`
- **Explanation:** `2` and `6` connect because their LCM is `6`; both values above the threshold form separate components.
