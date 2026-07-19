# Count Nodes With the Highest Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2049 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-nodes-with-the-highest-score/) |

## Problem Description

### Goal

A binary tree contains $n$ nodes labeled from $0$ through $n-1$ and is rooted at node $0$. The array `parents` encodes its edges: `parents[i]` gives the parent of node `i`, while `parents[0]` is `-1`.

To score a node, remove that node and every edge incident to it. The remaining nodes separate into one or more non-empty connected subtrees. Multiply the sizes of all those components to obtain the removed node's score. Determine the maximum score achieved anywhere in the tree and return how many nodes attain that same maximum.

### Function Contract

**Inputs**

- `parents`: an integer array of length $n$, where $2 \le n \le 10^5$, `parents[0] = -1`, and every later entry is a valid node index.
- `parents` describes a valid rooted binary tree, so each node has at most two children.

**Return value**

- Return the number of nodes whose removal produces the largest component-size product.

### Examples

**Example 1**

- Input: `parents = [-1,2,0,2,0]`
- Output: `3`
- Explanation: Nodes `1`, `3`, and `4` each score $4$, which is the maximum.

**Example 2**

- Input: `parents = [-1,2,0]`
- Output: `2`
- Explanation: Removing node `0` or node `1` produces score $2$; node `2` scores $1$.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Expressing every component with subtree sizes**

Build a child list from `parents`. If node `u` is removed, each child subtree becomes one component whose size is that child's subtree size. Unless `u` is the root, all nodes outside the subtree of `u` form one additional component of size `n - subtree_size[u]`. These components are disjoint and contain every node except `u`, so multiplying their nonzero sizes gives exactly the required score.

**Computing sizes after the children**

Create a traversal order with an explicit stack, then process that order in reverse. Every child is consequently handled before its parent, allowing `subtree_size[u]` to start at one and accumulate the already-known child sizes. During the same pass, multiply the child sizes and the nonzero parent-side size, then update both the largest score and the number of nodes tied at it.

This postorder calculation evaluates every component induced by every possible removal. Because each node's product is derived from exactly its resulting components, and the running counters compare all node scores, the final frequency is precisely the number achieving the global maximum.

#### Complexity detail

Building child lists, producing the traversal order, and processing nodes in reverse each visit every node and edge a constant number of times, for $O(n)$ time. Child lists, the order, stack, and subtree-size array require $O(n)$ space. The iterative traversal also avoids recursion-depth failure on a chain of up to $10^5$ nodes.

#### Alternatives and edge cases

- **Recursive postorder DFS:** This gives the same recurrence concisely, but a maximally deep valid tree can exceed Python's recursion limit.
- **Remove and recount each node:** Traversing the remaining components separately for every possible removal is correct but costs $O(n^2)$ time.
- The root has no parent-side component; multiplying by a fictitious zero would incorrectly erase its score.
- A leaf has no child components, so its score is solely the size $n-1$ of the parent-side component.
- Node labels are not guaranteed to place every parent before its children, so simply reversing array indices is not a valid postorder.

</details>
