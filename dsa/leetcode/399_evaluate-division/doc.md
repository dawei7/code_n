# Evaluate Division

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 399 |
| Difficulty | Medium |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/evaluate-division/) |

## Problem Description
### Goal
Each equation `[a, b]` supplies a positive ratio `a / b = value` between named variables. Ratios may be chained or inverted to infer relationships between other variables in the same connected component, and the supplied equations are consistent.

For every query `[x, y]`, return the inferred floating-point value of $x / y$. Return `-1.0` when either variable is unknown or no relationship path connects them. A known variable divided by itself equals `1.0`, but an entirely unknown $x / x$ still returns `-1.0`. Preserve query order and do not let one disconnected variable component influence another.

### Function Contract
**Inputs**

- `equations`: pairs `[a, b]` representing known divisions $a / b$
- `values`: the positive ratio corresponding to each equation
- `queries`: variable pairs whose division results are requested

**Return value**

- Return one floating-point result per query. Unknown variables or variables in disconnected relationship components produce `-1.0`.

### Examples
**Example 1**

- Input: `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]`
- Output: `[6.0,0.5,-1.0,1.0,-1.0]`

**Example 2**

- Input: `equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]`
- Output: `[3.75,0.4,5.0,0.2]`

**Example 3**

- Input: `equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","a"]]`
- Output: `[0.5,2.0,1.0]`

### Required Complexity

- **Time:** $O((e + q) \alpha(v))$
- **Space:** $O(v)$

<details>
<summary>Approach</summary>

#### General

**Attach a multiplicative weight to each parent link**

Use disjoint-set union over variables. For every variable `x`, store `weight[x] = x / parent[x]`. A root is its own parent with weight one. During path compression, multiply weights along the old path so the compressed value becomes `x / root`.

**Translate an equation into a root-to-root ratio**

For `a / b = value`, first find both roots and their compressed weights. If the roots differ, attach `root_a` below `root_b`. The required link weight is `root_a / root_b = value * weight[b] / weight[a]`, which makes the original equation remain true after the merge.

**Answer connected queries by dividing root weights**

If either queried variable is unknown or their roots differ, no relationship connects them and the result is `-1.0`. Otherwise both weights use the same root, so `a / b = (a / root) / (b / root) = weight[a] / weight[b]`.

**Why all implied equations remain consistent**

Each union adds exactly one equation-consistent link between two previously separate components. Path compression replaces a chain by a direct root link while preserving the product of its ratios. Inductively, every variable's stored root ratio equals the product implied by the input equations, so connected query quotients are correct.

#### Complexity detail

Let `e` be the equation count, `q` the query count, and `v` the number of variables. Weighted find and union have amortized $O(\alpha(v))$ time with path compression, where `α` is the inverse Ackermann function. Total time is $O((e + q) \alpha(v))$, and parent plus weight maps use $O(v)$ space.

#### Alternatives and edge cases

- **Weighted graph plus DFS or BFS per query:** is straightforward but may traverse $O(v + e)$ relationships for every query.
- **Precompute every connected pair:** gives constant-time queries but can require $O(v^2)$ time and space.
- **Floyd-Warshall-style closure:** is convenient only for small variable sets and costs cubic preprocessing.
- A known variable divided by itself equals `1.0`.
- An unknown variable divided by itself still returns `-1.0`.
- Variables in different components have no derivable ratio.
- Reciprocal edges are implicit in each stored equation.

</details>
