# Validate Binary Tree Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1361 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/validate-binary-tree-nodes/) |

## Problem Description

### Goal

Nodes are labeled from $0$ through $n-1$. Parallel arrays `leftChild` and `rightChild` describe directed child links: value `-1` means that side has no child, while any other value is the label of the corresponding left or right child.

Determine whether these links form exactly one valid binary tree containing all $n$ nodes. Thus one node must be the root, every other node must have exactly one parent, no node may have multiple parents, and following child links must reach every node without a cycle or disconnected component. Return a boolean result.

### Function Contract

**Inputs**

- `n`: the number of labeled nodes.
- `leftChild` and `rightChild`: length-$n$ arrays containing child labels or `-1`.

**Return value**

- `true` exactly when the described links form one binary tree over all $n$ nodes; otherwise `false`.

### Examples

**Example 1**

- Input: `n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]`
- Output: `true`

**Example 2**

- Input: `n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]`
- Output: `false`
- Explanation: node `3` is assigned to two parents.

**Example 3**

- Input: `n = 2, leftChild = [1,0], rightChild = [-1,-1]`
- Output: `false`
- Explanation: the two links form a cycle, leaving no root.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Enforce the parent rule while reading edges.** Allocate an indegree value for every node. For each nonnegative left or right child, increment that child's indegree. Reject immediately if it becomes greater than one, because a tree node other than the root cannot have multiple parents.

**Identify the unique root.** After processing all links, collect nodes with indegree zero. A valid tree has exactly one such node. Zero candidates indicates a directed cycle covering every component, while multiple candidates prove that at least two components are disconnected.

**Verify one connected acyclic traversal.** Start from the unique root and visit its nonnegative children with a stack or queue. If a node is encountered twice, reject the cycle or repeated path. Finally require exactly $n$ visited nodes. The indegree and unique-root checks constrain parentage, and the traversal proves reachability and absence of a reachable cycle; together these conditions are precisely one binary tree.

#### Complexity detail

There are at most $2n$ child entries. Building indegrees and traversing all reachable nodes each take $O(n)$ time. The indegree array, visited set, and traversal stack use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Union-find:** Union each parent-child edge while rejecting a repeated component connection, then verify one root and one component. This is near-linear but requires careful directed-parent checks in addition to connectivity.
- **Repeated parent scans:** Count a node's occurrences across both child arrays for every label. It is correct but costs $O(n^2)$ time.
- **DFS color states:** Three colors can detect directed cycles, but parent uniqueness and one-root coverage must still be checked.
- **Multiple parents:** Reject as soon as any child's indegree exceeds one, even if all nodes remain connected.
- **Disconnected cycle:** A unique apparent root elsewhere does not suffice; the final visited count detects unreachable cyclic components.
- **Single node:** With both child entries equal to `-1`, node `0` is a valid one-node tree.
- **Self-loop:** A node naming itself as a child creates a cycle and cannot form a valid tree.

</details>
