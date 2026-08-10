## General

**Process a node only after both subtrees**

Postorder traversal is defined as:

1. traverse the left subtree;
2. traverse the right subtree;
3. process the current root.

The nested `dfs` function implements exactly that order. It recursively visits `root.left`, recursively visits `root.right`, and appends `root.val` only after both calls return.

The difference from preorder is entirely in the append position. Moving `ans.append(root.val)` before the recursive calls would produce root-left-right; placing it between them would produce left-root-right.

**Use null children as the stopping condition**

When `root is None`, the helper returns without appending anything. A missing subtree has no values, so its postorder contribution is the empty sequence.

This base case lets every real node invoke both child traversals uniformly. Leaves call the helper on two null children and are appended after both immediate returns.

An empty input similarly calls `dfs(None)` once and returns the initially empty answer.

**What a completed call guarantees**

For any node `x`, after `dfs(x)` returns, the values appended during that call form exactly the postorder traversal of the subtree rooted at `x`.

For a null node, the claim is true because nothing is appended.

For a real node, assume the same claim holds for its child subtrees. The first recursive call appends the complete left postorder. The second appends the complete right postorder. Only then does the function append `x.val`. The combined sequence is left-right-root, which proves the claim for `x`.

Applying this structural argument at the original root proves the returned list is correct.

**Why every node is emitted exactly once**

A proper binary tree gives every non-root node exactly one parent path. The helper enters each real node through that path once. Only that node’s own frame appends its value, and it executes the append once after the child calls.

Values need not be unique. Two nodes storing the same integer are distinct traversal positions and correctly contribute duplicate entries.

**Trace the first example**

For the tree represented by `[1, null, 2, 3]`, the root’s left call contributes nothing. Its right call enters node `2`.

Node `2` first traverses its left child `3`. Node `3` has no children, so it appends `3`. Node `2` then has no right-subtree values and appends `2`. Only after the whole right subtree returns does the original root append `1`. The result is `[3, 2, 1]`.

This trace also illustrates why postorder naturally fits recursion: the call stack delays a node’s append until both nested tasks finish.

**One shared accumulator avoids repeated concatenation**

`ans` is allocated once and captured by `dfs`. Every frame appends directly to it.

An alternative recursive style could return separate left and right lists and concatenate them. In Python, repeatedly copying those lists can make a skewed tree take quadratic time. The shared accumulator preserves constant local work per node.

The algorithm reads child pointers and values but never changes the tree.

## Complexity detail

Let $n$ be the number of nodes and $h$ the maximum root-to-leaf node count.

Every real node is visited once, and each child-pointer check or append is constant time. Null calls also total only a constant multiple of $n$. Time is $O(n)$.

At most one recursion frame per node on the active root-to-current path exists simultaneously, so auxiliary stack space is $O(h)$. A balanced tree has $h=O(\log n)$, while a fully skewed tree has $h=n$.

The required output list stores $n$ integers. Excluding output, space matches the manifest’s $O(h)$. Including output, total additional storage is $O(n+h)=O(n)$.

The stated tree-size maximum of 100 keeps valid recursion well below Python’s normal recursion limit.

## Alternatives and edge cases

- **Visited-flag stack:** Push `(node, processed)` records. On first encounter, schedule the root after its children; on the processed encounter, append it. It is iterative and uses $O(h)$ to $O(n)$ stack space.
- **One stack plus previous pointer:** Descend left, inspect the stack top, and process it after its right child has been visited. It uses $O(h)$ space with delicate state logic.
- **Modified preorder then reverse:** Visit root-right-left iteratively and reverse the collected values. It is simple but needs a stack and a final reversal.
- **Morris postorder:** Create temporary predecessor threads and emit reversed right boundaries. A fully pointer-reversing version can reach $O(1)$ auxiliary space excluding output.
- **Empty tree:** The base case leaves `ans` empty.
- **Single node:** Both child calls return before its value is appended.
- **Only left children:** Values appear from the deepest leaf back to the root.
- **Only right children:** The same deepest-to-root pattern results.
- **Duplicate values:** Every node contributes independently; postorder does not deduplicate.
- **Malformed cyclic structure:** Recursion would not terminate, but the contract supplies a tree.
- **Runtime dependencies:** The source uses `Optional` and `List` without imports. The platform supplies `TreeNode`; standalone Python also needs `from typing import List, Optional`.
