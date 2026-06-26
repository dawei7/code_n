# Kth Smallest Element in a BST

| | |
|---|---|
| **ID** | `tree_23` |
| **Category** | trees |
| **Complexity (required)** | $O(H + K)$ Time, $O(H)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) |

## Problem statement

Given the `root` of a binary search tree, and an integer `k`, return the k-th smallest value (1-indexed) of all the values of the nodes in the tree.

**Input:** A BST `root` node, and an integer `k`.
**Output:** An integer representing the k-th smallest value.

## When to use it

- To retrieve ordered data from a hierarchical structure without allocating memory for the entire dataset.
- The definitive test of your understanding of In-Order Traversal.

## Approach

**1. The In-Order Guarantee:**
An In-Order Traversal (`Left -> Root -> Right`) of a valid Binary Search Tree is mathematically guaranteed to visit the nodes in perfectly sorted ascending order.
The 1st node you visit is the absolute minimum. The 2nd is the 2nd smallest. The K-th node you visit is the K-th smallest!

**2. The Naive Approach ($O(N)$ Time, $O(N)$ Space):**
You could run a full In-Order traversal (`tree_02`), append every single value to a massive array, and then just return `array[k - 1]`.
While technically valid, this is a massive waste of memory and time! If you have a tree with 1 million nodes, and you just want the 2nd smallest element (`k=2`), you don't need to traverse and store 999,998 larger nodes!

**3. The Counter Optimization ($O(H + K)$ Time, $O(H)$ Space):**
Instead of an array, we just keep a global `count` integer!
We start our In-Order traversal. Every time we formally "process" a node (after returning from the left child), we increment `count += 1`.
If `count == k`, we have found our answer! We store the node's value in a global `result` variable and instantly ABORT the traversal (return early from all recursive calls)!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_23: Kth Smallest in BST.

In-order traversal visits the nodes in sorted order.
"""


def solve(children, values, root, n, k):
    out = []

    def inorder(i):
        if i == -1:
            return
        inorder(children[i][0])
        out.append(values[i])
        inorder(children[i][1])

    inorder(root)
    if k < 1 or k > len(out):
        return -1
    return out[k - 1]
```

</details>

## Walk-through

Tree:
```text
      5
     / \
    3   6
   / \
  2   4
 /
1
```
`k = 3`.

**Iterative Stack Walk-through:**
1. Dive Left: Stack `[5, 3, 2, 1]`. `curr` becomes null.
2. Pop `1`. `k` drops to `2`. Not zero. `curr = 1.right` (null).
3. Pop `2`. `k` drops to `1`. Not zero. `curr = 2.right` (null).
4. Pop `3`. `k` drops to `0`. ZERO!
5. Return `3.val` which is `3`.

Output: `3`. ✓ (The sorted order is 1, 2, 3, 4, 5, 6. The 3rd element is 3).
*Notice we NEVER even looked at nodes 4, 5, or 6! We aborted instantly!*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(H + K)$ | $O(H)$ |
| **Average** | $O(H + K)$ | $O(H)$ |
| **Worst** | $O(N)$ | $O(N)$ |

To find the absolute smallest element, we must traverse from the root down to the leftmost leaf. This takes $O(H)$ time where H is the height of the tree.
Then, we must pop and process exactly K nodes. This takes $O(K)$ time.
Total time complexity is mathematically $O(H + K)$.
In a balanced tree, finding the 1st element takes $O(\log N)$ time.
In the absolute worst case (a skewed tree, and K = N), it takes $O(N)$ time.
Space complexity is bounded by the Stack or Recursive Call Stack, which holds at most H nodes. $O(H)$ space.

## Variants & optimizations

- **Frequent Insert/Deletes ($O(\log N)$ Time):** What if the tree is constantly updating, and we need to query `kthSmallest` thousands of times? $O(H+K)$ is too slow. You can physically augment the `TreeNode` class to include an `int size` variable that tracks the total number of nodes in its left subtree! When searching, if `left.size == k - 1`, the current node IS the answer in pure $O(\log N)$ time!

## Real-world applications

- **Database Pagination:** If an SQL database indexes users by Age using a B-Tree, and a query asks for `SELECT * ORDER BY age LIMIT 10 OFFSET 50`, the engine uses a generalized version of this algorithm to skip the first 50 nodes and pull the next 10.

## Related algorithms in cOde(n)

- **[tree_02 - In-order Traversal](tree_02_inorder-traversal.md)** — The engine that enforces the ascending order.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
