# Lowest Common Ancestor of a Binary Tree

| | |
|---|---|
| **ID** | `tree_17` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |

## Problem statement

Given a binary tree, find the Lowest Common Ancestor (LCA) of two given nodes `p` and `q` in the tree.
The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).
It is mathematically guaranteed that `p` and `q` exist in the tree, and `p != q`.

**Input:** A binary tree `root` node, and two target nodes `p` and `q`.
**Output:** The `TreeNode` representing the LCA.

## When to use it

- To find the shortest path or distance between two arbitrary nodes in a tree.
- One of the most frequently asked, elegant recursive DFS problems in all of computer science.

## Approach

**1. The "Reporting" Recursion:**
Imagine a boss (the Root) asking their two managers (Left Child, Right Child): "Go search your departments and tell me if you find employee P or employee Q!"
We write a recursive DFS function. When it visits a node:
- If the node is `null`, return `null`. (Dead end, found nobody).
- If the node IS `p` or IS `q`, return the node itself! (I found one of them! Report it up!).

**2. The Three Scenarios for a Parent:**
When a parent node receives the reports from its left and right subtrees, it faces exactly 3 scenarios:

- **Scenario 1: Both left and right returned a non-null node.**
  The left subtree found `p`. The right subtree found `q`.
  What does this mean? It means THIS VERY NODE is the point where the paths diverge! THIS node is mathematically the Lowest Common Ancestor! The parent returns ITSELF up the chain!
  
- **Scenario 2: One side returned a node, the other returned `null`.**
  The left subtree found someone (maybe `p`, maybe `q`, or maybe the LCA was already found deep down and is being bubbled up). The right subtree found nothing.
  What does the parent do? It just passes the successful report UP the chain! Return the non-null side!
  
- **Scenario 3: Both sides returned `null`.**
  Nobody was found in either subtree. Return `null` up the chain.

**3. The "Descendant of Itself" Edge Case:**
What if `p = 5` and `q = 4`, but `4` is actually a direct child of `5`?
When the DFS hits `5`, it instantly returns `5`! It completely stops searching and never even finds `4`!
Is this a bug? NO! It's a genius feature! If `q` is a child of `p`, then `p` mathematically IS the Lowest Common Ancestor! By instantly returning `p`, it correctly bubbles `p` all the way to the root as the answer!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_17: Lowest Common Ancestor.

Return the index of the LCA of two nodes in a binary tree.
Walk the tree; find the path from the root to each node, and
take the last common node on both paths.
"""


def solve(children, root, n, p, q):
    """Return the LCA of p and q in a binary tree."""
    if root == -1:
        return -1

    def path_to(u, target):
        if u == -1:
            return None
        if u == target:
            return [u]
        left = path_to(children[u][0], target)
        if left is not None:
            return [u] + left
        right = path_to(children[u][1], target)
        if right is not None:
            return [u] + right
        return None

    pp = path_to(root, p)
    pq = path_to(root, q)
    if pp is None or pq is None:
        return -1
    last = -1
    for a, b in zip(pp, pq):
        if a == b:
            last = a
        else:
            break
    return last
```

</details>

## Walk-through

Tree:
```text
      3
    /   \
   5     1
  / \   / \
 6   2 0   8
    / \
   7   4
```
`p = 6`, `q = 4`.

1. **`dfs(3)`:** Calls left (5) and right (1).
   2. **`dfs(1)`:** Not P or Q. Calls left (0) and right (8). Both return null.
      - Returns `null`.
   3. **`dfs(5)`:** Not P or Q. Calls left (6) and right (2).
      4. **`dfs(6)`:** Wait! Node is P (6)! Instantly returns node `6`.
      5. **`dfs(2)`:** Calls left (7) and right (4).
         6. **`dfs(7)`:** Nulls out. Returns `null`.
         7. **`dfs(4)`:** Node is Q (4)! Returns node `4`.
      - `dfs(2)` receives `null` from left, `4` from right.
      - Returns `4` upwards.
   - `dfs(5)` receives `6` from left, `4` from right!
   - Both are NON-NULL! Node 5 realizes IT IS THE LCA!
   - Returns `node 5` upwards!
- `dfs(3)` receives `node 5` from left, `null` from right.
- Returns `node 5` upwards.

Root call returns `node 5`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

In the worst case (where `p` and `q` are deep leaves), the DFS visits every single node in the tree once. Time complexity is exactly $O(N)$.
Space complexity is bounded by the recursive call stack $O(H)$. Average case is $O(\log N)$ for balanced trees. Worst case is $O(N)$ for skewed trees.

## Variants & optimizations

- **LCA of a Binary Search Tree (BST) ($O(\log N)$):** If the tree is a BST, you do NOT need DFS! You just start at the root. If both P and Q are smaller than the root, go left. If both are larger, go right. The FIRST node you hit where P and Q split directions is mathematically guaranteed to be the LCA! This takes $O(\log N)$ time and $O(1)$ space!
- **LCA using Parent Pointers:** If every `TreeNode` has a `parent` pointer, this problem instantly transforms into **Intersection of Two Linked Lists (`linkedlist_06`)**! You just trace P up to the root, trace Q up to the root, and find the first shared node!

## Real-world applications

- **CSS / DOM Event Bubbling:** Finding the exact HTML DOM container that encapsulates two clicked elements to apply a shared UI visual effect.
- **Git Merge / Version Control:** If branch A and branch B have diverged, Git must find their Lowest Common Ancestor commit to perform an intelligent 3-way merge!

## Related algorithms in cOde(n)

- **[tree_03 - Post-order Traversal](tree_03_postorder-traversal.md)** — The core mechanism (process children first, then evaluate the parent) used to "bubble up" the reports.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
