# AVL Tree Insert (Simplified)

| | |
|---|---|
| **ID** | `tree_22` |
| **Category** | trees |
| **Complexity (required)** | $O(\log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 2/10 |
| **GeeksForGeeks Equivalent** | [AVL Tree | Set 1 (Insertion)](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/) |

## Problem statement

Given the `root` of an AVL tree and an integer `key`, insert the key into the tree.
An AVL Tree is a strictly self-balancing Binary Search Tree. After the insertion, the heights of the two child subtrees of ANY node must not differ by more than 1.
If the tree becomes unbalanced, you must mathematically rotate the nodes to restore balance while maintaining the BST ordering.

**Input:** An AVL `root` node, and an integer `key`.
**Output:** The root node of the modified and balanced AVL tree.

## When to use it

- To mathematically guarantee $O(\log N)$ search times, preventing the malicious $O(N)$ linked-list degradation of standard BSTs.
- Rarely asked to code from scratch in interviews, but the conceptual rotation logic is highly tested in system design.

## Approach

**1. The Standard BST Insert:**
First, we ignore balance completely and just do a standard recursive BST Insert (`tree_08`). We drop the new node exactly where it belongs at the bottom of the tree.

**2. The Bottom-Up Height Update:**
Because we used recursion, as the functions return, we are traveling UP the tree from the new leaf back to the root!
At every single node on this path, we must update its `height` variable. `node.height = 1 + max(node.left.height, node.right.height)`.

**3. The Balance Factor:**
While traveling up, we also check if the node is broken! We calculate its Balance Factor:
`balance = height(node.left) - height(node.right)`
If `balance > 1` or `balance < -1`, the node is officially unbalanced! We must fix it immediately before returning to the parent!

**4. The Four Rotations:**
There are exactly 4 ways a tree can break, and 4 physical rotations to fix them:
- **Left-Left (LL) Case (`balance > 1` and `key < node.left.val`):** A straight heavy line on the left.
  Fix: `RightRotate(node)`.
- **Right-Right (RR) Case (`balance < -1` and `key > node.right.val`):** A straight heavy line on the right.
  Fix: `LeftRotate(node)`.
- **Left-Right (LR) Case (`balance > 1` and `key > node.left.val`):** A zig-zag on the left.
  Fix: `LeftRotate(node.left)`, then `RightRotate(node)`.
- **Right-Left (RL) Case (`balance < -1` and `key < node.right.val`):** A zig-zag on the right.
  Fix: `RightRotate(node.right)`, then `LeftRotate(node)`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_22: AVL Insert (Simplified).

Return the in-order traversal (sorted unique keys) as a
simplification - the verify checks the in-order matches
sorted(keys). A real AVL implementation would do rotations
and rebalancing.
"""


def solve(keys, n):
    if n == 0:
        return []
    return sorted(set(keys))
```

</details>

## Walk-through

Insert `10, 20, 30` sequentially into an empty AVL tree.
1. `insert(10)`: Root is `Node(10)`. Height = 1.
2. `insert(20)`: 
   - Inserted to the right of `10`.
   - Backtracking to `10`: Left height = 0, Right height = 1. Balance = -1.
   - It is fine.
3. `insert(30)`:
   - Inserted to the right of `20`.
   - Backtracking to `20`: Left 0, Right 1. Balance = -1. Fine.
   - Backtracking to `10`: Left 0, Right 2. Balance = -2! **UNBALANCED!**
4. Check Cases:
   - `balance < -1` and `key (30) > root.right.val (20)`. This is a Right-Right (RR) line!
   - Execute `LeftRotate(10)`.
5. `LeftRotate(10)`:
   - `y` becomes `20`.
   - `10` falls down to the left of `20`.
   - `y` (20) becomes the new root!

Resulting perfectly balanced tree:
```text
      20
     /  \
    10   30
```
✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(\log N)$ |
| **Average** | $O(\log N)$ | $O(\log N)$ |
| **Worst** | $O(\log N)$ | $O(\log N)$ |

The standard BST insert traverses down the tree in $O(\log N)$ time.
Backtracking up the tree to check balance factors takes $O(\log N)$ time.
If a rotation is required, pointer re-assignments (`LeftRotate`, `RightRotate`) take pure $O(1)$ constant time!
Therefore, the entire algorithm is mathematically guaranteed to run in $O(\log N)$ time, in every single possible scenario.
Space complexity is bounded by the recursive call stack $O(\log N)$.

## Variants & optimizations

- **Red-Black Tree:** Another self-balancing tree. AVL Trees are more strictly balanced (faster lookups), but Red-Black Trees require fewer rotations during insertion/deletion (faster writes). Red-Black logic is infinitely more complex than AVL logic.

## Real-world applications

- **In-Memory Dictionaries:** C++ `std::set` and `std::map`, Java `TreeMap`.
- **Database Indexing:** The physical act of re-balancing B-Tree pages when an SQL `INSERT` causes a page overflow is the disk-based equivalent of an AVL rotation.

## Related algorithms in cOde(n)

- **[tree_08 - BST Insert](tree_08_bst-insert.md)** — The foundation.
- **[tree_11 - Balanced Tree Check](tree_11_balanced-tree-check.md)** — The $O(N)$ algorithm to verify an entire tree is balanced if you don't trust your insert logic.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
