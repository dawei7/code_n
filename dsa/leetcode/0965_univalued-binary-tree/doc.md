# Univalued Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 965 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [univalued-binary-tree](https://leetcode.com/problems/univalued-binary-tree/) |

## Problem Description

### Goal

A binary tree is called uni-valued when every node in the entire tree stores the same value. Given the tree's `root`, determine whether it has this property.

Return `true` only if every existing node agrees with the root's value; otherwise return `false`. Missing children are structural gaps rather than nodes and therefore contribute no value to compare. The input always contains at least one node, so `root` itself supplies the required reference value.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ nodes and having height $H$.
- The node count satisfies $1 \le N \le 100$.
- Every node value satisfies $0 \le \texttt{Node.val} < 100$.
- In serialized cases, the tree is represented in level order and `null` denotes a missing child.

**Return value**

Return `true` if all $N$ nodes have one common value; otherwise return `false`.

### Examples

**Example 1**

- Input: `root = [1,1,1,1,1,null,1]`
- Output: `true`

**Example 2**

- Input: `root = [2,2,2,5,2]`
- Output: `false`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Use the root as the reference.** Since the tree is nonempty, store `root.val` before traversal. Every node must equal this single value; no frequency table or ordering property is needed.

**Traverse each existing node once.** Maintain a depth-first stack beginning with `root`. Pop a node, return `false` immediately if its value differs from the reference, and push each non-null child. If the traversal finishes without finding a mismatch, every node has been checked and the tree is uni-valued.

**Why early rejection is safe.** One differing node is enough to violate the definition, regardless of values elsewhere. Conversely, reaching the end proves that every node belongs to the visited set and matched `root.val`, so returning `true` is sufficient and necessary.

#### Complexity detail

Each of the $N$ nodes is pushed, popped, and compared once, giving $O(N)$ time. A depth-first traversal retains at most $O(H)$ pending nodes, so auxiliary space is $O(H)$.

#### Alternatives and edge cases

- **Recursive depth-first search:** Require the current node to match the root and recursively validate both children. This is equally direct but uses the language call stack.
- **Breadth-first search:** A queue also checks every node in $O(N)$ time, but its space is the maximum tree width rather than the height.
- **Repeated subtree scans:** Recheck every descendant for each possible subtree root. This remains correct but can take $O(N^2)$ time on a chain.
- **Single node:** A one-node tree is uni-valued by definition.
- **Zero value:** `0` is a valid node value and must not be treated as a missing node.
- **Sparse shape:** Missing children do not affect the result; only existing node values matter.

</details>
