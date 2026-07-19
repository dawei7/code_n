# Maximum Genetic Difference Query

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1938 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Bit Manipulation, Depth-First Search, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-genetic-difference-query/) |

## Problem Description
### Goal
A rooted tree contains $N$ nodes numbered from $0$ through $N-1$. A node's
number is also its unique genetic value. The `parents` array gives each node's
parent, with `-1` identifying the one root. The genetic difference between two
values is their bitwise XOR.

Each query is `[node, value]`. Consider every node on the inclusive path from
`node` upward to the root, and XOR its genetic value with `value`. Return the
largest such difference for every query, preserving the original query order.

### Function Contract
**Inputs**

- `parents`: a length-$N$ parent array describing one rooted tree, where
  $2 \le N \le 10^5$. Exactly one entry is `-1`; every other parent is a valid
  node index.
- `queries`: $Q$ pairs `[node, value]`, where
  $1 \le Q \le 3\cdot10^4$, `node` is a valid tree index, and
  $0 \le \texttt{value} \le 2\cdot10^5$.

Let $B$ be the number of bits needed to represent the largest node index or
query value; under the constraints, $B \le 18$.

**Return value**

- A length-$Q$ list whose entry for each query is the maximum of
  `value XOR ancestor` over the queried node and all of its ancestors,
  including the root.

### Examples
**Example 1**

- Input: `parents = [-1, 0, 1, 1]`,
  `queries = [[0, 2], [3, 2], [2, 5]]`
- Output: `[2, 3, 7]`

**Example 2**

- Input: `parents = [3, 7, -1, 2, 0, 7, 0, 2]`,
  `queries = [[4, 6], [1, 15], [0, 5]]`
- Output: `[6, 14, 7]`

**Example 3**

- Input: `parents = [-1, 0]`, `queries = [[1, 3]]`
- Output: `[3]`
