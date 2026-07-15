# Maximum Product of Splitted Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1339 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree with positive node values, remove exactly one edge. This separates the original tree into two non-empty subtrees. Compute the sum of the node values in each resulting component and multiply those two sums.

Choose the edge that makes this product as large as possible. Maximize the full integer product first, then return that maximum modulo $10^9+7$; comparing products after reducing them modulo the constant would not preserve their true order.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where $2\le n\le5\cdot10^4$ and $1\le\texttt{node.val}\le10^4$.

**Return value**

The maximum product of the two component sums obtainable by removing one edge, reduced modulo $10^9+7$ only after the maximum is chosen.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5,6]`
- Output: `110`
- Explanation: One optimal cut creates components with sums 11 and 10.

**Example 2**

- Input: `root = [1,null,2,3,4,null,null,5,6]`
- Output: `90`

**Example 3**

- Input: `root = [1,2]`
- Output: `2`
- Explanation: The only edge separates sums 1 and 2.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Treat every non-root subtree as one possible cut**

Removing the edge above a node separates that node's complete subtree from the rest of the tree. If its sum is $s$ and the total tree sum is $S$, the product for that edge is $s(S-s)$. Thus every candidate can be evaluated once all subtree sums and $S$ are known.

Perform an iterative postorder traversal. Push each node first as unprocessed; when it is popped in that state, schedule it as processed after its children. When the processed entry is reached, both child sums are already available, so store their sum plus the node value. This avoids recursion depth failures on a legal 50,000-node chain.

The root is processed last, yielding $S$. Evaluate $s(S-s)$ for every stored non-root subtree sum and keep the largest full integer product. Each removable edge corresponds to exactly one non-root node, so this checks every legal split exactly once. Apply the modulus only to the final maximum.

#### Complexity detail

Each node is pushed and processed a constant number of times, giving $O(n)$ time. The traversal stack, subtree-sum map, and collected sums use $O(n)$ space.

#### Alternatives and edge cases

- **Two recursive traversals:** One traversal can compute $S$ and another can find the best subtree product, but a skewed legal tree may exceed Python's recursion limit.
- **Repeated subtree summation:** Recomputing all descendants for every candidate edge is correct but takes $O(n^2)$ time on a chain.
- **Two nodes:** There is only one legal edge to remove.
- **Skewed tree:** Iterative postorder handles maximum depth without call-stack growth.
- **Equal products:** Only the product value matters; the particular edge need not be returned.
- **Modulo timing:** Choose the maximum using unreduced products and take modulo afterward.
- **Positive values:** Every component sum is positive, so every legal cut has a positive product.

</details>
