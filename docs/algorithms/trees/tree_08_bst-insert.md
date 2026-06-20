# Binary Search Tree (BST) Insert

| | |
|---|---|
| **ID** | `tree_08` |
| **Category** | trees |
| **Complexity (required)** | $O(H)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) |

## Problem statement

Given the `root` node of a Binary Search Tree (BST) and a `value` to insert into the tree. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.
You must insert the new node in a way that perfectly maintains the BST mathematical invariant properties.

**Input:** A BST `root` node, and an integer `val`.
**Output:** The root node of the modified BST.

## When to use it

- To build a Binary Search Tree from scratch.
- An extremely common interview warm-up that tests your understanding of tree pointers and the BST property.

## Approach

**1. The Leaf Guarantee:**
In a standard, un-balanced BST, there are infinite valid places to insert a new value that satisfy the mathematical property.
However, there is exactly ONE place that is absolutely trivial to find: **As a new Leaf Node at the very bottom of the tree!**
We never need to restructure the tree, swap nodes, or shift subtrees. We just drop the new node at the bottom where it naturally falls.

**2. The "Failed Search" Strategy:**
How do we find where it naturally falls? We just pretend we are SEARCHING for the value (`tree_06`)!
We start at the root.
- If `val` < current, we go left.
- If `val` > current, we go right.
Because the value doesn't exist in the tree, our search will eventually hit a dead end (a `null` pointer).
That exact `null` spot is mathematically the perfect place to attach our new node!

**3. Pointer Management:**
When doing this iteratively, we must be careful! If `curr` becomes `null`, we've fallen off the tree, and we can't attach our new node because we lost the reference to our parent!
Therefore, we must use a trailing pointer `parent` to keep track of the last valid node we were standing on before we fell off.
Once we fall off, we attach the new node to either `parent.left` or `parent.right` depending on the value!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_08: BST Insert.

Walk a BST, insert at the first empty child slot.
"""


def solve(children, values, root, n, key):
    new_children = [list(c) for c in children]
    new_values = list(values)
    if n == 0:
        new_values.append(key)
        new_children.append([-1, -1])
        return new_children, new_values
    u = root
    while True:
        if key == new_values[u]:
            return new_children, new_values
        if key < new_values[u]:
            left, right = new_children[u]
            if left == -1:
                new_idx = len(new_values)
                new_values.append(key)
                new_children.append([-1, -1])
                new_children[u][0] = new_idx
                return new_children, new_values
            u = left
        else:
            left, right = new_children[u]
            if right == -1:
                new_idx = len(new_values)
                new_values.append(key)
                new_children.append([-1, -1])
                new_children[u][1] = new_idx
                return new_children, new_values
            u = right
```

</details>

## Walk-through

`Tree = [4, 2, 7, 1, 3]`, `val = 5`.
Tree structure:
```text
      4
    /   \
   2     7
  / \
 1   3
```

1. `curr = 4`, `parent = None`.
   - `val (5) > 4`. Go right.
   - `parent` becomes `4`. `curr` becomes `7`.
2. `curr = 7`.
   - `val (5) < 7`. Go left.
   - `parent` becomes `7`. `curr` becomes `curr.left` (which is `None`).
3. Loop terminates because `curr is None`!
4. We fell off at `parent = 7`.
5. Check: `val (5) < parent.val (7)`.
6. Attach: `parent.left = new TreeNode(5)`.

New Tree:
```text
      4
    /   \
   2     7
  / \   /
 1   3 5
```
Returns root `4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

Let H be the height of the tree.
The iterative traversal drops down exactly one level per step until it hits a leaf. The number of steps is exactly the depth of the insertion point.
Therefore, time complexity is exactly $O(H)$.
If the tree is balanced, H = log_2 N. If it's heavily skewed, H = N.
Space complexity for the Iterative version is $O(1)$ constant time because we only allocate memory for the single new node. (The recursive version takes $O(H)$ Call Stack space).

## Variants & optimizations

- **AVL Tree Insert (`tree_22`):** This simple insert is fast, but inserting sorted data (`1, 2, 3, 4, 5`) degrades the tree into an $O(N)$ linked list. An AVL insert does this exact algorithm, but then traces backwards up the tree, calculating the "Balance Factor" at each node, and mathematically rotating nodes to guarantee the tree's height remains strictly $O(\log N)$!

## Real-world applications

- **Set / Map implementations:** In C++, `std::set` and `std::map` are internally implemented as Red-Black Trees (a self-balancing variant of the BST). Every time you do `set.insert(5)`, an identical variant of this algorithm is executing under the hood!

## Related algorithms in cOde(n)

- **[tree_06 - BST Search](tree_06_bst-search.md)** — The read-only algorithm that uses the exact same `while curr is not None` pathing logic.
- **[tree_15 - BST Delete](tree_15_bst-delete.md)** — The incredibly complicated sister operation (deleting a node is much harder because you must restructure the children!).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
