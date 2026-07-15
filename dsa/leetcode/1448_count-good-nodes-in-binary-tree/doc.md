# Count Good Nodes in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1448 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) |

## Problem Description
### Goal

A node in a binary tree is good when no node on the path from the root to that
node has a value greater than the node's own value. The path includes both the
root and the node itself. Equality is allowed, so a node whose value ties the
largest earlier value on its path is good.

Given the root of a non-empty binary tree, return the total number of good
nodes. The root is always good because its root-to-root path contains no other
value that could exceed it.

### Function Contract
**Inputs**

- `root`: the root node of a non-empty binary tree containing $n$ nodes, where
  $1 \le n \le 10^5$.
- Each node has an integer `val` satisfying
  $-10^4 \le \text{val} \le 10^4$ and optional `left` and `right` children.
- Serialized examples represent the tree in level order and use `null` for a
  missing child; the function itself receives the constructed root node.

Let $h$ be the height of the tree.

**Return value**

Return the number of nodes whose value is at least every value on their path
from `root`.

### Examples
**Example 1**

- Input: `root = [3, 1, 4, 3, null, 1, 5]`
- Output: `4`
- Explanation: The root, the left leaf with value `3`, and the nodes with
  values `4` and `5` are good. The other nodes have a larger ancestor.

**Example 2**

- Input: `root = [3, 3, null, 4, 2]`
- Output: `3`
- Explanation: Equal value `3` is allowed, and its child `4` is also good;
  the node `2` is below an ancestor with value `3`.

**Example 3**

- Input: `root = [1]`
- Output: `1`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reduce an entire path to one sufficient value**

To decide whether a node is good, the individual order of its ancestors no
longer matters once their maximum value is known. If the current node's value
is at least that path maximum, no ancestor is greater and the node is good. If
it is smaller, the ancestor that established the maximum proves that it is not
good. Thus each traversal state needs only a node and the maximum value seen
on the path reaching it.

**Carry the maximum through an iterative depth-first traversal**

Initialize a stack with `(root, root.val)`. When a state is removed, compare
`node.val` with its stored path maximum and increment the answer when
`node.val >= path_maximum`. Then compute
`next_maximum = max(path_maximum, node.val)` and attach that value to each
existing child pushed onto the stack.

Using an explicit stack avoids Python recursion-depth failure on a legal tree
that degenerates into a chain of up to $10^5$ nodes. DFS order is otherwise
unimportant because each child receives state derived only from its own
root-to-parent path.

**Why the carried state gives the exact count**

The initial state is correct for the root: its stored maximum equals the only
value on its path. Suppose a node's stored value is the maximum on its full
root-to-node path. Comparing the node against it is then exactly the definition
of goodness, with `>=` correctly admitting ties. For either child, taking the
maximum of the current state and `node.val` yields the maximum on the extended
root-to-child path, so every pushed state has the same property.

By induction, the comparison is correct for every visited node. A tree gives
each non-root node exactly one parent, so the traversal pushes and evaluates
each node exactly once. Incrementing precisely on the good-node comparison
therefore produces the required total without omissions or duplicates.

#### Complexity detail

Each of the $n$ nodes is pushed, removed, compared, and expanded once, giving
$O(n)$ time. The explicit DFS stack holds at most $O(n)$ node-state pairs in
the worst case, so the general auxiliary-space bound is $O(n)$. More tightly,
its size depends on the traversal frontier and is $O(h)$ for the usual
depth-first accounting, where $h$ can equal $n$ for a skewed tree. No output
collection proportional to the node count is constructed.

#### Alternatives and edge cases

- **Breadth-first traversal:** A queue carrying `(node, path_maximum)` uses the
  same $O(n)$ time and is equally correct. Its frontier can contain an entire
  wide level, whereas DFS commonly retains a depth-sized frontier.
- **Recursive depth-first search:** Passing the maximum as an argument gives a
  compact recurrence and $O(h)$ call-stack space, but Python's recursion limit
  makes it unsafe for a legal $10^5$-node chain without environment changes.
- **Rescan every root-to-node path:** Retaining each path and recomputing its
  maximum is correct, but a skewed tree has total path length
  $1+2+\cdots+n=O(n^2)$.
- **Root node:** It is always counted because its value equals the maximum of
  its one-node path.
- **Equal ancestor value:** Use `>=`, not `>`; a tie does not introduce a
  greater path value.
- **Negative values:** Initialize from `root.val` rather than zero, since zero
  would incorrectly reject good nodes in an all-negative tree.
- **Branch independence:** A large value in one subtree must not affect nodes
  in another subtree; each child state inherits only its own ancestors.
- **Skewed tree:** The iterative implementation avoids recursion overflow and
  still visits every node once.

</details>
