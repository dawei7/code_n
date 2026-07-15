# Sum of Nodes with Even-Valued Grandparent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1315 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, identify every node whose grandparent has an even value. A node's grandparent is the parent of its parent, so the root and its direct children never qualify.

Add the values of all qualifying nodes and return the total. The parity of the qualifying node and its parent does not matter; only the grandparent's value determines whether the node contributes. Return 0 when no node has an even-valued grandparent.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where $1\le n\le10^4$.
- Every node value is between 1 and 100 inclusive.

**Return value**

The sum of `node.val` over all nodes whose existing grandparent has an even value.

### Examples
**Example 1**

- Input: `root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]`
- Output: `18`

**Example 2**

- Input: `root = [1]`
- Output: `0`

**Example 3**

- Input: `root = [2,3,5,7,11,13,17]`
- Output: `48`
- Explanation: The four grandchildren have even-valued grandparent 2, so they contribute $7+11+13+17$.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Carry the two ancestor values during traversal**

Traverse the tree with an explicit stack. Alongside each node, store the value of its parent and grandparent, using null when an ancestor does not exist. When a node is removed from the stack, add its value exactly when the stored grandparent is non-null and even.

For either child, the current node becomes the child's parent and the current parent becomes the child's grandparent. Push that shifted ancestor state with the child. This local update preserves the actual two-generation relationship on every root-to-node path.

Every tree node is reached once through its unique parent. The stored grandparent is therefore exactly the parent of that unique parent, and the test includes precisely the nodes required by the contract. Nodes at depth zero or one carry a null grandparent and correctly contribute nothing.

#### Complexity detail

The traversal visits each of the $n$ nodes once and performs constant work per node, taking $O(n)$ time. The explicit stack holds at most $O(n)$ entries in the worst case. On a balanced tree its maximum size is proportional to the tree height or frontier, but $O(n)$ is the general bound.

#### Alternatives and edge cases

- **Recursive depth-first search:** Passing parent and grandparent values as parameters is equally linear, but a legal 10000-node chain can exceed the language recursion limit.
- **Breadth-first search:** Queue entries can carry the same two ancestor values and preserve the $O(n)$ bounds.
- **Repeated parent searches:** Locating each node's parent and then grandparent by searching from the root is correct but can take $O(n^2)$ time on a skewed tree.
- **Root and children:** They have no grandparent and never contribute, even when the root itself is even.
- **Odd parent:** A node still contributes when its grandparent is even; its parent's parity is irrelevant.
- **No qualifying node:** The accumulator remains 0.
- **Repeated values:** Nodes are counted by position and ancestry, not deduplicated by value.

</details>
