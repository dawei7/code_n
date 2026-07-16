# Find Root of N-Ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1506 |
| Difficulty | Medium |
| Topics | Hash Table, Bit Manipulation, Tree, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/find-root-of-n-ary-tree/) |

## Problem Description
### Goal

An N-ary tree consists of nodes that each store a unique integer value and a list of zero or more children. Instead of receiving a pointer to the root, you are given an array containing every node object in the tree. The nodes may appear in any order, but their child references still describe the original directed parent-to-child edges.

Find and return the one node that is the root. The input is guaranteed to describe one valid N-ary tree, so exactly one node has no parent. LeetCode's displayed level-order serialization is only a way to construct tests; the array supplied to the function is randomly ordered.

### Function Contract
**Inputs**

Let $N$ be the number of nodes in the tree.

- Native `findRoot(tree)` receives an array of all $N$ node objects in arbitrary order. Every node exposes a unique integer `val` and a `children` list containing references to its children.
- The directed references form one valid N-ary tree: the root has no parent and every other node appears exactly once among all child lists.
- The app-local `solve(tree)` receives the same information as `[value, child_values]` records. Values identify nodes unambiguously because they are unique.

**Return value**

Return the root node. The app-local adapter returns that node's integer value.

### Examples
**Example 1**

- Input: `tree = [[3, [5, 6]], [2, []], [4, []], [1, [3, 2, 4]], [5, []], [6, []]]`
- Output: `1`
- Explanation: Every value except `1` occurs in a child list, so the node with value `1` is the root.

**Example 2**

- Input: `tree = [[8, []], [9, []], [7, [8, 9]]]`
- Output: `7`

**Example 3**

- Input: `tree = [[42, []]]`
- Output: `42`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Turn parent cancellation into a root signature**

In a valid tree, every non-root node occurs twice across the supplied information: once as an element of `tree`, and once as a child of its unique parent. The root occurs only in `tree`, because no parent refers to it.

Bitwise XOR cancels equal values because $x \mathbin{\mathrm{XOR}} x = 0$, while zero is neutral. XOR every node value into one accumulator, then XOR every referenced child value into the same accumulator. Each non-root value cancels with its second occurrence. The sole value left is the root's value.

The app-local representation stores child values directly, so it performs this cancellation without reconstructing node objects. The platform-native implementation makes a second linear pass to return the actual node whose `val` equals the remaining value.

**Why order and shape do not affect the result**

XOR is associative and commutative. Therefore neither the random order of the node array nor the order of siblings changes the accumulator. Branching factors and tree depth are also irrelevant: the proof depends only on the one-parent property.

For each non-root node $v$, the accumulator contains exactly two copies of its unique value, and those copies cancel. The root value appears exactly once, so the final accumulator identifies precisely the required node. The guarantee that values are unique makes the native lookup unambiguous.

#### Complexity detail

Across all nodes, the child lists contain exactly $N-1$ references. Scanning the $N$ nodes, all $N-1$ edges, and then at most $N$ nodes to recover the native object takes $O(N)$ time.

The accumulator and loop variables occupy constant auxiliary space, independent of $N$. The input node array and child lists already belong to the caller and are not counted as extra storage, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Child-value hash set:** insert every child value, then return the node whose value is absent. This is straightforward and remains $O(N)$ time, but consumes $O(N)$ extra space.
- **Sum cancellation:** subtract every child value from the sum of all node values. It expresses the same invariant, but fixed-width languages may overflow unless they use a sufficiently wide type; XOR avoids that concern.
- **Repeated parent search:** for each candidate, scan every child list to see whether it has a parent. It uses constant space but can require $O(N^2)$ time.
- **Traversal from each candidate:** trying to infer the root by repeatedly exploring descendants does unnecessary work because the input already exposes every incoming edge.
- **Single node:** no child value is present, so its value remains in the accumulator and that node is returned.
- **Root appears last:** array position is irrelevant; the algorithm does not assume the first node is the root.
- **Wide or deep trees:** only the total number of nodes and edges matters; the algorithm uses neither recursion nor a traversal stack.
- **Nonconsecutive values:** cancellation relies on equality, not on values forming a range.
- **Random node order:** commutativity makes all permutations equivalent.

</details>
