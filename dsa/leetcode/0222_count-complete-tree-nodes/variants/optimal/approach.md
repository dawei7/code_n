## General
A complete tree fills every level except possibly the last, and fills that last level from left to right. This structure guarantees that at each node, at least one child subtree is perfect and can be counted without visiting its nodes.

Measure the height obtained by repeatedly following left children in both child subtrees.

- If the heights are equal at `h`, the left subtree is perfect with $2^{h} - 1$ nodes. Counting it together with the current root contributes $2^{h}$; recurse only into the right subtree.
- If the left height is greater, the right subtree is perfect at its smaller height. Count the root and that perfect right subtree as `2 ** right_height`, then recurse into the left subtree.

Why does the comparison identify the perfect side? Equal heights mean the last level has reached the right subtree, so every position in the left subtree is filled. Unequal heights mean the last level has not reached the right subtree's bottom level, making that right subtree perfect one level shorter. Completeness also passes to the one subtree that remains for recursion.

For a six-node tree `[1,2,3,4,5,6]`, the child left-heights match, so the root plus perfect left subtree contribute four nodes. Recursing on the right subtree counts its two nodes, producing six without traversing the left subtree individually.

## Complexity detail
Tree height is $O(\log n)$. Each recursive level follows a left spine in $O(\log n)$ time, and recursion descends through at most one subtree per level, giving $O(\\log^{2} n)$ time. Recursive stack space is $O(\log n)$; an iterative form can use $O(1)$ auxiliary pointer state.

## Alternatives and edge cases
- Plain DFS or BFS works for arbitrary binary trees but visits all `n` nodes.
- Treating the entire complete tree as perfect overcounts a partially filled final level.
- Binary-searching the occupied positions on the last level also gives $O(\\log^{2} n)$ time but needs bit-path existence checks.
- Empty and one-node trees are immediate base cases.
- Power expressions should use integer shifts or integer exponentiation rather than floating-point arithmetic.
