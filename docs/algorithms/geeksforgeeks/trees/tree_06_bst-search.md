# Binary Search Tree (BST) Search

| | |
|---|---|
| **ID** | `tree_06` |
| **Category** | trees |
| **Complexity (required)** | $O(H)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) |

## Problem statement

Given the `root` of a Binary Search Tree (BST) and an integer `val`.
Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

**Input:** A BST `root` node, and an integer `val`.
**Output:** The target `Node`, or `null`.

## When to use it

- To perform blazing-fast lookups in sorted, hierarchical data.
- The fundamental building block that proves why BSTs are mathematically superior to Linked Lists for searching.

## Approach

**1. The BST Property:**
A Binary Search Tree is not just a random tree. It has a strict mathematical invariant:
For EVERY node, all values in its **Left Subtree** are strictly LESS than the node's value. All values in its **Right Subtree** are strictly GREATER than the node's value.

**2. The Binary Search Analogy:**
This property mirrors exactly how a standard Binary Search (`search_02`) works on a sorted array!
When we are at a `current_node`, we compare its value to our `target`.
- If `target == current_node.val`: We found it! Return the node.
- If `target < current_node.val`: The target is smaller. Because of the BST property, we are 100% mathematically certain that if the target exists, it MUST be in the Left Subtree! We completely discard the Right Subtree and move to `current_node.left`.
- If `target > current_node.val`: The target is larger. It MUST be in the Right Subtree! Discard the Left Subtree and move to `current_node.right`.

**3. Recursion vs Iteration:**
Because we only ever move down a single path (we never branch or backtrack), we don't actually need recursion! A simple `while` loop that updates a pointer achieves the exact same logic but with $O(1)$ memory instead of $O(H)$ Call Stack memory.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_06: BST Search.

Walk a binary search tree, comparing the target to each node's
value, going left or right accordingly.
"""


def solve(children, values, root, n, target):
    u = root
    while u is not None and u != -1:
        if values[u] == target:
            return u
        left, right = children[u]
        if target < values[u]:
            u = left if left != -1 else None
        else:
            u = right if right != -1 else None
    return -1
```

</details>

## Walk-through

`Tree = [4, 2, 7, 1, 3]`, `target = 2`.
Tree structure:
```text
      4
    /   \
   2     7
  / \
 1   3
```

1. `curr` points to `4`.
   - `4 == 2`? No.
   - `2 < 4`? Yes! The target must be to the left.
   - `curr = curr.left` (points to `2`).
2. `curr` points to `2`.
   - `2 == 2`? Yes! Match found!
   - Return the node `2`. ✓

`target = 5`.
1. `curr` points to `4`.
   - `5 > 4`. Go right. `curr` points to `7`.
2. `curr` points to `7`.
   - `5 < 7`. Go left. `curr = curr.left`.
3. Node `7` has no left child! `curr.left` is `None`.
4. Loop terminates because `curr is None`.
5. Return `None`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

Let H be the height of the tree.
At each step, we drop exactly one level deeper into the tree. We never revisit nodes. The maximum number of comparisons is exactly equal to the height of the tree.
Therefore, time complexity is $O(H)$.
If the tree is perfectly balanced (e.g. an AVL or Red-Black tree), the height H = log_2 N. Time is $O(\log N)$.
**WORST CASE:** If elements were inserted into the tree in sorted order (e.g., 1, 2, 3, 4, 5), the tree degrades into a straight line (a Linked List). The height becomes H = N. Time degrades to $O(N)$!
Space complexity for the Iterative version is strictly $O(1)$.

## Variants & optimizations

- **Closest Value in BST:** Instead of returning exactly when `curr.val == val`, you maintain a `closest_val` variable. At each node, you check if `abs(curr.val - target) < abs(closest_val - target)`. You still move left or right exactly the same way!

## Real-world applications

- **Database Indexing:** B-Trees (a generalized version of BSTs) are the fundamental data structure used by SQL databases (like MySQL and PostgreSQL) to execute `SELECT * WHERE id = 5` in micro-seconds instead of scanning the whole database.

## Related algorithms in cOde(n)

- **[tree_08 - BST Insert](tree_08_bst-insert.md)** — The sister algorithm. If a search fails and hits `None`, that exact `None` spot is mathematically exactly where you would insert the target to maintain the BST!
- **[search_02 - Binary Search](../searching/search_02_binary-search.md)** — The array-based equivalent of this exact logic.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
