# Delete Node in a BST

| | |
|---|---|
| **ID** | `tree_15` |
| **Category** | trees |
| **Complexity (required)** | $O(H)$ Time, $O(H)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) |

## Problem statement

Given a `root` node reference of a BST and a `key`, delete the node with the given key in the BST. Return the `root` node reference (possibly updated) of the BST.
The deletion must perfectly maintain the Binary Search Tree properties.

**Input:** A BST `root` node, and an integer `key`.
**Output:** The root node of the modified BST.

## When to use it

- To complete the holy trinity of Data Structure operations (Search, Insert, Delete).
- A rigorous test of your ability to handle complex pointer re-assignments and edge cases in a tree topology.

## Approach

**1. Find the Node:**
First, we must actually find the node to delete! This is a simple binary search (`tree_06`).
- If `key < root.val`, the node to delete is in the left subtree: `root.left = delete(root.left, key)`.
- If `key > root.val`, it is in the right subtree: `root.right = delete(root.right, key)`.

**2. The Three Cases of Deletion:**
Once we find the node (`root.val == key`), we face 3 entirely different topological scenarios!

- **Case 1: The node is a Leaf (No children).**
  This is trivial! Just delete it. We return `null` to the parent, effectively severing the connection.

- **Case 2: The node has exactly ONE child.**
  Also easy! If we delete the node, its single child will be left hanging. We simply take that child and plug it directly into the deleted node's parent! We return the non-null child.

- **Case 3: The node has TWO children.**
  This is the nightmare scenario! We cannot return both children to the parent (a binary tree parent can only have one left pointer!). We must completely restructure the tree!
  Instead of deleting the node structurally, we **Overwrite its Value**!
  What value can we steal that mathematically maintains the BST property?
  We need a number slightly larger than the current node, but smaller than everything else in the right subtree. This is called the **In-Order Successor**!
  The In-Order Successor is found by going into the Right Subtree, and traveling LEFT as far as physically possible.
  We copy the Successor's value into our current node. Then, we recursively call the delete function on the Right Subtree to physically delete the original Successor node!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_15: BST Delete.

Delete a key from a BST. The setup picks a key that is in
the tree; the canonical solve removes it. Three cases:
leaf (just drop), one child (replace with child), two
children (replace with inorder successor).

Tree is given as a binary shape: children[i] = [left, right]
where -1 means absent.
"""


def solve(children, values, root, n, key):
    """Delete `key` from the BST. Return (new_children, new_values)."""
    new_children = [list(c) for c in children]
    new_values = list(values)
    if n == 0:
        return new_children, new_values
    # Find the node to delete and its parent.
    u = root
    parent = -1
    while u != -1 and new_values[u] != key:
        parent = u
        u = new_children[u][0] if key < new_values[u] else new_children[u][1]
    if u == -1:
        return new_children, new_values  # not found
    left = new_children[u][0]
    right = new_children[u][1]
    if left == -1 and right == -1:
        # Leaf case.
        if parent == -1:
            return [], []
        if new_children[parent][0] == u:
            new_children[parent][0] = -1
        else:
            new_children[parent][1] = -1
    elif left == -1 or right == -1:
        # One child case.
        child = left if left != -1 else right
        if parent == -1:
            new_children[u] = [-1, -1]
        elif new_children[parent][0] == u:
            new_children[parent][0] = child
        else:
            new_children[parent][1] = child
    else:
        # Two children case: replace value with inorder successor
        # and unlink the successor.
        succ_parent = u
        succ = right
        while new_children[succ][0] != -1:
            succ_parent = succ
            succ = new_children[succ][0]
        new_values[u] = new_values[succ]
        if succ_parent == u:
            new_children[u][1] = new_children[succ][1]
        else:
            new_children[succ_parent][0] = new_children[succ][1]
    return new_children, new_values
```

</details>

## Walk-through

Tree:
```text
      5
    /   \
   3     6
  / \     \
 2   4     7
```
`delete(5)`:
1. `root` is `5`. `key == 5`. Node found!
2. Does it have 2 children? Yes (`3` and `6`). (Case 3).
3. Find successor: Go right to `6`, then go left as far as possible.
   `6` has no left child. So `6` IS the successor!
4. Overwrite root's value: `root.val` becomes `6`.
5. Recursively delete the successor's value (`6`) from the right subtree:
   - Call `deleteNode(root.right, 6)`.
   - `root` is `6`. `key == 6`. Node found!
   - Does `6` have 1 child? Yes, right child `7`. (Case 2).
   - Return `7`.
6. `root.right` becomes `7`.

Resulting Tree:
```text
      6
    /   \
   3     7
  / \
 2   4
```
BST properties perfectly maintained! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(\log N)$ |
| **Average** | $O(\log N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The algorithm requires traversing down the tree to find the node, and potentially traversing down further to find the successor.
The maximum number of nodes visited is the height of the tree $O(H)$.
In a balanced tree, time complexity is $O(\log N)$.
In a skewed linked-list-like tree, time complexity degrades to $O(N)$.
Space complexity is bounded by the recursive call stack $O(H)$, which is $O(\log N)$ average and $O(N)$ worst-case. (This can be optimized to $O(1)$ Space using an Iterative approach with parent pointers, but the code becomes monstrously complex).

## Variants & optimizations

- **In-Order Predecessor:** Instead of stealing the smallest value from the right subtree (Successor), you can mathematically steal the LARGEST value from the LEFT subtree (Predecessor)! Go left once, then right as far as possible. It works identically!

## Real-world applications

- **Database Table Row Deletion:** In SQL databases using B-Tree indexing, deleting a row uses a generalized version of this exact algorithm to restructure the tree pages and physically merge nodes if a page becomes too empty.

## Related algorithms in cOde(n)

- **[tree_08 - BST Insert](tree_08_bst-insert.md)** — The much simpler operation of adding a node.
- **[tree_22 - AVL Insert](tree_22_avl-insert-simplified.md)** — In a self-balancing tree, after you delete the node using this algorithm, you MUST trace backwards up the tree and perform physical rotations to rebalance it!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
