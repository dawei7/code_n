# Smallest Missing Genetic Value in Each Subtree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2003 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search, Union-Find |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/) |

## Problem Description

### Goal

A family tree contains $N$ nodes numbered from $0$ through $N-1$ and is rooted at node $0$. Array `parents` gives the parent of every node, with `parents[0] = -1`. Each node $i$ carries the distinct positive genetic value `nums[i]`, drawn from $1$ through $10^5$.

For every node $i$, consider all genetic values stored at $i$ and its descendants. Find the smallest positive integer absent from that subtree and return all $N$ answers in node order.

### Function Contract

**Inputs**

- `parents`: a valid rooted-tree parent array of length $N$, where $2 \le N \le 10^5$.
- `nums`: $N$ pairwise-distinct integers from $1$ through $10^5$.

**Return value**

Return an array `answer` of length $N$ in which `answer[i]` is the smallest positive genetic value missing from the subtree rooted at node $i$.

### Examples

**Example 1**

- Input: `parents = [-1, 0, 0, 2], nums = [1, 2, 3, 4]`
- Output: `[5, 1, 1, 1]`
- Explanation: The root contains values $1$ through $4$, while every other subtree omits $1$.

**Example 2**

- Input: `parents = [-1, 0, 1, 0, 3, 3], nums = [5, 4, 6, 2, 1, 3]`
- Output: `[7, 1, 1, 4, 2, 1]`
- Explanation: The subtree at node $3$ contains $\{1,2,3\}$, and the leaf holding $1$ is missing $2$.

**Example 3**

- Input: `parents = [-1, 2, 3, 0, 2, 4, 1], nums = [2, 3, 4, 5, 6, 7, 8]`
- Output: `[1, 1, 1, 1, 1, 1, 1]`
- Explanation: Genetic value $1$ is absent from the whole tree, so it is absent from every subtree.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Identify the only subtrees that can exceed one.** If the tree has no node carrying genetic value $1$, every answer is immediately $1$. Otherwise, a subtree can contain $1$ only when its root is the node holding $1$ or one of that node's ancestors. Initialize every answer to $1$ and process only this ancestor path.

**Grow the covered subtree while walking upward.** Build children lists and start at the node whose value is $1$. For the current path node, traverse its subtree and add genetic values from nodes not visited during an earlier step. Then move to its parent. The previously covered subtree remains included, while the traversal adds precisely the parent's value and any sibling branches. A visited array ensures each tree node is incorporated at most once.

**Maintain the missing value monotonically.** Keep a set of all values incorporated so far and a pointer `missing`, initially $1$. After each expansion, advance the pointer while it belongs to the set, then assign it to the current path node. The covered values are exactly that node's subtree, so the first absent positive value is correct. Moving upward only adds values, so `missing` never needs to decrease and advances at most $N+1$ times overall.

#### Complexity detail

Building child lists takes $O(N)$ time and space. Across every incremental traversal, each node is marked and its children are expanded once. The missing-value pointer advances monotonically, so all path steps together take $O(N)$ time. Children, visited flags, the value set, and the answer use $O(N)$ space.

#### Alternatives and edge cases

- **Traverse every subtree independently:** Collecting values and finding the missing positive for each root can take $O(N^2)$ time on a chain.
- **Merge a set from every child:** Small-to-large set merging can solve the general subtree problem in $O(N\log N)$ time, but does not exploit the special role of genetic value $1$.
- If value $1$ is absent from the entire tree, every answer is $1$.
- Nodes outside the ancestor path of value $1$ cannot have an answer larger than $1$.
- When value $1$ is at the root, only the root needs a nontrivial computation.
- Distinct genetic values eliminate multiplicity concerns when values are added to the global set.

</details>
