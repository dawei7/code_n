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

### Required Complexity
- **Time:** $O((N+Q)B)$
- **Space:** $O(NB+Q)$

<details>
<summary>Approach</summary>

#### General

**Attach queries to their tree nodes**

Build child lists from `parents` and group each query with its target node,
retaining the query's original index. This lets a single tree traversal answer
queries exactly when their complete ancestor path is known.

**Maintain the active root-to-node path**

Traverse the tree depth first. On entering a node, insert its numeric label
into a counted binary trie. At that moment, the trie contains precisely the
queried node and all of its ancestors: earlier sibling subtrees have already
been removed, while descendants have not yet been entered. Answer every query
attached to the node, then visit its children. On leaving the node, decrement
its trie counts.

Use explicit enter and exit events on a stack rather than recursive calls, so
a chain of up to $10^5$ nodes cannot overflow Python's recursion limit.

**Choose opposite bits greedily**

For a query value, walk the trie from the highest bit downward. At each bit,
prefer an active branch whose bit is opposite the query bit, because that sets
the current result bit to one. If no counted node exists on that branch, take
the matching branch. Higher XOR bits dominate every combination of lower
bits, so this greedy choice yields the maximum XOR among all active ancestors.

The DFS path invariant restricts candidates to exactly the permitted nodes,
and the trie walk maximizes against that set. Storing results by original query
index preserves input order even though queries are processed in traversal
order.

#### Complexity detail

Each node label is inserted once and removed once, with $B$ trie steps per
operation. Each of the $Q$ queries also takes $B$ steps, giving
$O((N+Q)B)$ time. The child lists and grouped queries use $O(N+Q)$ space, and
the trie can contain $O(NB)$ nodes across all inserted labels. The traversal
stack uses $O(N)$ space, so the total is $O(NB+Q)$.

#### Alternatives and edge cases

- **Walk parents for every query:** Check the target and repeatedly follow
  `parents` to the root. This is simple and correct, but a chain with a query
  at every node takes $O(NQ)$ time.
- **Persistent trie per node:** Derive each node's trie version from its
  parent's version. Queries are fast and online, but persistence stores
  $O(NB)$ nodes and is more involved than the reversible DFS trie.
- The queried node and root are both eligible candidates.
- The root may have any node index; it is identified by its `-1` parent rather
  than assumed to be node zero.
- Queries on different branches must not see sibling or cousin labels.
- Multiple queries attached to one node share the same active trie but retain
  separate answers and order.
- A query value of zero asks for the numerically largest ancestor label.
- The bit width must cover query values as well as node labels.

</details>
