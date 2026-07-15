# Delete Tree Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1273 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-tree-nodes/) |

## Problem Description

### Goal

A valid tree with `nodes` vertices is rooted at node $0$. Array `parent` describes its edges: `parent[i]` is the parent of node $i$, while `parent[0] = -1`. Array `value` assigns an integer value to each corresponding node.

Delete every subtree whose node values sum to zero. Deleting a subtree removes its root and every descendant, so none of those nodes can remain independently. After all zero-sum subtrees have been removed, return the number of nodes still present in the rooted tree.

### Function Contract

**Inputs**

- `nodes`: the node count $n$, where $1 \le n \le 10^4$.
- `parent`: a length-$n$ parent array defining a valid tree rooted at $0$, with `parent[0] = -1`.
- `value`: a length-$n$ array with $-10^5 \le \texttt{value[i]} \le 10^5$.

**Return value**

- Return the number of nodes remaining after every zero-sum subtree is deleted.

### Examples

**Example 1**

- Input: `nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]`
- Output: `2`

**Example 2**

- Input: `nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]`
- Output: `6`

**Example 3**

- Input: `nodes = 1, parent = [-1], value = [0]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Evaluate children before their parent**

Build a child list for every node from `parent`. Traverse the tree in postorder without recursion: first record a root-first order with a stack, then process that order in reverse. For each node, combine its own value with the already computed sums of all children. At the same time, combine one for the node itself with the retained counts of its children.

If the resulting subtree sum is zero, set its retained count to zero. Its numerical sum remains zero when propagated upward, exactly as the deleted subtree contributed before deletion. Otherwise keep the accumulated node count.

Postorder guarantees that every child's complete subtree is known before its parent is evaluated. Thus the computed sum at each node equals the sum of precisely that original subtree. A zero sum deletes exactly all of its nodes; a nonzero sum retains its root and only the child subtrees not already deleted. Induction from leaves to the root proves that the retained count stored at node $0$ is the requested answer.

#### Complexity detail

Building child lists, constructing the traversal order, and processing it in reverse each touch every node and edge a constant number of times, for $O(n)$ time. Child lists, traversal order, stack, sums, and counts use $O(n)$ space.

#### Alternatives and edge cases

- **Recursive postorder DFS:** It expresses the same recurrence directly but may exceed Python's recursion depth on a long chain.
- **Recompute every subtree separately:** It is correct but revisits descendants and can require $O(n^2)$ time.
- **Rebuild child lists by concatenation:** Repeatedly copying a growing sibling list is correct but quadratic for a wide star.
- **Zero-valued leaf:** Its one-node subtree is removed.
- **Zero-sum root:** The entire tree disappears and the answer is `0`.
- **Nested zero-sum subtrees:** A deleted child's sum is zero, so its removal does not change the ancestor's original subtree sum.
- **Negative values:** Only the complete subtree sum matters; individual signs do not decide deletion.

</details>
