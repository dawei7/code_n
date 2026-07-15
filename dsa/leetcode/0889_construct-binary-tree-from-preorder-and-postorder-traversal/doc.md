# Construct Binary Tree from Preorder and Postorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 889 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Divide and Conquer, Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) |

## Problem Description
### Goal
Two integer arrays describe the same binary tree with distinct node values. `preorder` lists each root before its left and right subtrees, while `postorder` lists both subtrees before their root.

Reconstruct and return a binary tree whose preorder traversal is exactly `preorder` and whose postorder traversal is exactly `postorder`. The traversals are guaranteed to be mutually valid. They may not determine a unique tree—for example, the side of a single child is ambiguous—and any tree matching both arrays is acceptable.

### Function Contract
Let $n=\lvert\texttt{preorder}\rvert=\lvert\texttt{postorder}\rvert$.

**Inputs**

- `preorder`: the preorder traversal of $n$ distinct node values, where $1 \leq n \leq 30$ and every value lies between $1$ and $n$.
- `postorder`: the postorder traversal of the same binary tree, containing the same $n$ distinct values.

**Return value**

Return the root of any binary tree whose preorder and postorder traversals equal the given arrays.

### Examples
**Example 1**

- Input: `preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]`
- Output: `[1,2,3,4,5,6,7]`

**Example 2**

- Input: `preorder = [1], postorder = [1]`
- Output: `[1]`

**Example 3**

- Input: `preorder = [1,2], postorder = [2,1]`
- Output: `[1,2]`

`[1,null,2]` is also valid because both possible child orientations have the same two traversals.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Locate each subtree's postorder boundary**

The first unused preorder value is the root of the current subtree. If more nodes remain in that subtree, the next preorder value is the root of its first child subtree. Because postorder places a subtree root last, an index map from value to postorder position identifies exactly where that first child subtree ends.

**Recurse over disjoint postorder intervals**

Maintain one advancing `preorder_index`. For a current postorder interval `[left, right]`, create the next preorder value as the root. The position of the following preorder value closes the first child interval, which is constructed as `root.left`. If nodes remain between that interval and the root at `postorder[right]`, construct them as `root.right`.

The chosen root is correct because preorder always visits it first. The next preorder value must begin the first child subtree, and its unique postorder position gives that entire subtree's final element, so the interval split cannot mix nodes from the two children. Recursively applying the same argument produces both required traversals. When only one child exists, assigning it to the left is one of the explicitly permitted answers.

#### Complexity detail

Building the postorder index map costs $O(n)$ time. Every node is created once and every interval boundary is found in constant time, so reconstruction also takes $O(n)$ time. The map, returned nodes, and recursion stack use $O(n)$ space in the worst case.

#### Alternatives and edge cases

- **Search postorder for every split:** Omitting the index map keeps the same recursion but can cost $O(n^2)$ time on a skewed tree.
- **Slice arrays recursively:** This is concise, but repeated slicing and searches also cause $O(n^2)$ copying and lookup work.
- **Iterative stack construction:** A stack synchronized with postorder can build a valid tree in $O(n)$ time, though the completion condition is less direct.
- **Single node:** The shared value is the root and both children are absent.
- **Single-child ambiguity:** Either left or right placement is valid as long as both traversals remain unchanged.
- **Distinct values:** Uniqueness makes the postorder index map and every subtree boundary unambiguous.
- **Full two-child node:** Nodes after the first child interval and before the current postorder root necessarily form the second child subtree.

</details>
