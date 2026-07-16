# Kth Ancestor of a Tree Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1483 |
| Difficulty | Hard |
| Topics | Binary Search, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search, Breadth-First Search, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) |

## Problem Description
### Goal

A rooted tree contains `n` nodes numbered from `0` through `n - 1`. It is supplied as a `parent` array: `parent[i]` gives the direct parent of node `i`, and node `0` is the root with `parent[0] = -1`.

Build a `TreeAncestor` object that answers repeated ancestor queries. For `getKthAncestor(node, k)`, follow the path from `node` toward the root and return the node reached after exactly `k` parent steps. If that many ancestors do not exist, return `-1`.

### Function Contract
**Inputs**

Let $Q$ be the number of calls to `getKthAncestor`.

- Constructor `TreeAncestor(n, parent)`:
  - `n`: the node count, with $1 \le n \le 5 \cdot 10^4$.
  - `parent`: an array of length $n$ with `parent[0] = -1`.
  - For every $1 \le i < n$, $0 \le \texttt{parent[i]} < n$; the array describes a rooted tree whose root is node `0`.
- Method `getKthAncestor(node, k)`:
  - `node`: a node identifier with $0 \le \texttt{node} < n$.
  - `k`: the requested ancestor distance, with $1 \le k \le n$.
- At most $5 \cdot 10^4$ queries are issued.
- The app-local `solve(n, parent, operations)` receives calls as `["getKthAncestor", [node, k]]` and returns one result per call.

**Return value**

Each query returns the node exactly `k` edges above `node`, or `-1` if the path reaches above the root. The app-local wrapper returns these query results in operation order.

### Examples
**Example 1**

- Constructor: `TreeAncestor(7, [-1,0,0,1,1,2,2])`
- Operations: `getKthAncestor(3, 1)`, `getKthAncestor(5, 2)`, `getKthAncestor(6, 3)`
- Output: `[1,0,-1]`
- Explanation: Node `3` has parent `1`; node `5` reaches root `0` in two steps; node `6` has depth two, so a third ancestor does not exist.

### Required Complexity
- **Time:** $O((n + Q) \log n)$
- **Space:** $O(n \log n)$

<details>
<summary>Approach</summary>

#### General

**Why direct parent links are insufficient for many queries**

The `parent` array answers a one-step query immediately, but following it `k` times costs $O(k)$. With both the tree and query count as large as $5 \cdot 10^4$, a deep chain queried repeatedly would require quadratic total work. Preprocessing longer jumps lets each query skip most intermediate nodes.

**Defining the binary-lifting table**

Let `up[j][v]` denote the ancestor of node `v` exactly $2^j$ edges above it, or `-1` when that ancestor does not exist. Level zero is the supplied parent array because $2^0 = 1$.

For every higher level, split a $2^j$ jump into two consecutive $2^{j-1}$ jumps:

```text
halfway = up[j - 1][v]
up[j][v] = -1 if halfway == -1 else up[j - 1][halfway]
```

By induction on `j`, every stored entry has the stated jump length. Only `n.bit_length()` levels are needed because every legal `k` is at most `n`.

**Decomposing a query into power-of-two jumps**

Every positive integer `k` has a unique binary representation. Scan its set bits from low to high. When bit `j` is set, replace the current node with `up[j][node]`, advancing exactly $2^j$ edges. The sum of those chosen powers is `k`, so if all jumps exist, the final node is exactly the requested ancestor.

If any jump produces `-1`, the path has already moved above the root. No later jump can restore a node, so the query returns `-1` immediately.

**Why combining jumps preserves the answer**

Before processing any bits, the current node is zero edges above the query node. After processing a set of bits, it is the ancestor at a distance equal to the sum of their powers, because each table lookup continues upward from the result of the preceding lookup. After all bits, that accumulated distance is exactly `k`. Together with the table induction, this proves every returned node is correct and every missing ancestor is reported as `-1`.

#### Complexity detail

The table has $O(\log n)$ levels and $n$ entries per level, so construction takes $O(n \log n)$ time and space. Each query inspects at most $O(\log n)$ bits and uses constant work per set bit, for $O(\log n)$ time. Across $Q$ queries, total time is $O((n + Q) \log n)$ and stored state is $O(n \log n)$.

#### Alternatives and edge cases

- **Walk through direct parents:** Follow `parent[node]` exactly `k` times. It uses only $O(n)$ stored tree data but costs $O(k)$ per query and can become $O(nQ)$ on a chain.
- **Memoize only requested jumps:** Cache ancestors encountered by queries. This may help repeated identical requests but offers no worst-case guarantee when queries cover many nodes and distances.
- **Depth-first traversal with path stacks:** An offline batch of known queries can answer ancestors while traversing the tree, but the required class must support online calls after construction.
- **Euler-tour level-ancestor structures:** More advanced preprocessing can improve constants or theoretical query bounds, but binary lifting is simpler and satisfies the constraints.
- **Querying the root:** Every legal positive `k` returns `-1` for node `0`.
- **Distance equals depth:** The answer is the root.
- **Distance exceeds depth:** Some selected jump reaches `-1`, and the answer is `-1`.
- **Power-of-two distance:** A single table lookup supplies the result.
- **Non-power-of-two distance:** Multiple set bits compose disjoint jump lengths whose sum is exactly `k`.
- **Single-node tree:** The table contains only the root's `-1` parent and every query returns `-1`.

</details>
