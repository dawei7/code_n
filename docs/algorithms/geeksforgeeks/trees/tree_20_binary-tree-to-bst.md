# Convert Binary Tree to BST

| | |
|---|---|
| **ID** | `tree_20` |
| **Category** | trees |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Binary Tree to Binary Search Tree Conversion](https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/) |

## Problem statement

Given a standard Binary Tree, convert it into a Binary Search Tree in such a way that keeps the original topological structure of the tree entirely intact.
(You cannot restructure the pointers or nodes; you can only overwrite the values inside the nodes).

**Input:** A binary tree `root` node.
**Output:** The same `root` node, but with values rearranged to form a BST.

## When to use it

- To test the absolute fundamental definition of an In-Order traversal: **An In-Order Traversal of a Binary Search Tree always yields a perfectly sorted array.**
- To quickly salvage unorganized tree data without needing to re-allocate new memory nodes or restructure complex pointers.

## Approach

**1. The In-Order Property:**
If we have a valid BST, and we perform an In-Order traversal (`Left -> Root -> Right`), the values we read will be perfectly sorted from smallest to largest!
This mathematical property is a two-way street! If we have the exact topological shape of a tree, and we do an In-Order traversal, and we physically WRITE a sorted list of values into the nodes as we visit them, the resulting tree is mathematically guaranteed to be a valid BST!

**2. The Three-Step Process:**
1. **Extract:** Traverse the original binary tree (using ANY traversal, e.g., Pre-Order or BFS) and extract all the node values into an array.
2. **Sort:** Sort the extracted array of values in ascending order.
3. **Inject:** Perform a strict In-Order traversal (`tree_02`) on the original tree. As you visit each node, overwrite its value with the next value from your perfectly sorted array!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_20: Binary Tree to BST.

Convert a binary tree to a binary SEARCH tree holding the
same values. In-order walk to collect nodes; sort values;
walk in-order again, replacing each node's value with
the next sorted value.
"""


def solve(children, values, root, n):
    if n == 0 or root == -1:
        return [], []
    out = []

    def collect(i):
        if i == -1:
            return
        collect(children[i][0])
        out.append(i)
        collect(children[i][1])
    collect(root)
    sorted_vals = sorted(values)
    new_values = list(values)
    for idx, node in enumerate(out):
        new_values[node] = sorted_vals[idx]
    return list(children), new_values
```

</details>

## Walk-through

Original Tree (Not a BST):
```text
      10
     /  \
    30   15
   /      \
  20       5
```

1. **Extract:** Read all values. `values = [10, 30, 20, 15, 5]`.
2. **Sort:** `values = [5, 10, 15, 20, 30]`.
3. **Inject (In-Order Traversal):**
   - Go to deepest left node: `20`. Overwrite with `values[0]` (`5`).
   - Go to its parent: `30`. Overwrite with `values[1]` (`10`).
   - Right child of `30` is null.
   - Go to root: `10`. Overwrite with `values[2]` (`15`).
   - Go to right subtree, `15`. Go deep left (null).
   - Process `15`: Overwrite with `values[3]` (`20`).
   - Go to right child: `5`. Overwrite with `values[4]` (`30`).

Final Resulting Tree:
```text
      15
     /  \
    10   20
   /      \
  5       30
```
It is a perfect BST! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

Step 1 (Extraction) takes $O(N)$ time.
Step 2 (Sorting) takes $O(N \log N)$ time.
Step 3 (Injection) takes $O(N)$ time.
The overall time complexity is dominated by the sorting step: $O(N \log N)$.
Space complexity is strictly $O(N)$ because we must create an auxiliary array to hold all N values for sorting.

## Variants & optimizations

- **Convert Sorted Array to BST:** If you are given a sorted array and asked to construct a brand new balanced BST from scratch (you are NOT constrained by a pre-existing topology), you do not use this algorithm! You just pick the middle element as the root, and recursively build the left and right halves. Takes exactly $O(N)$ time!
- **In-Place Restructuring (Day-Stout-Warren Algorithm):** You can actually convert a Binary Tree into a perfectly balanced BST in strictly $O(N)$ time and $O(1)$ space by using tree rotations to turn the tree into a linked list (a "Vine"), and then rotating it back into a balanced tree. This is incredibly complex.

## Real-world applications

- **Data Sanitization:** In game development, if a spatial partitioning tree becomes corrupted due to physics engine glitches, you can rapidly salvage the node bounding boxes and re-sort them without allocating any new memory.

## Related algorithms in cOde(n)

- **[tree_02 - In-order Traversal](tree_02_inorder-traversal.md)** — The engine that enforces the BST ordering property.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
