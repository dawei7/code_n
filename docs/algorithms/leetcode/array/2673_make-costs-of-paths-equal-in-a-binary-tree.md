# Make Costs of Paths Equal in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2673 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy, Tree, Binary Tree |
| Official Link | [make-costs-of-paths-equal-in-a-binary-tree](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/) |

## Problem Description & Examples
### Goal
Given a complete binary tree represented by a 0-indexed array `cost`, where `cost[i]` is the value of the `i`-th node. The root is at index 0, and for any node `i`, its left child is at `2*i + 1` and its right child is at `2*i + 2`. The objective is to determine the minimum total amount that must be added to the costs of various nodes such that the sum of costs along every path from the root to any leaf node becomes equal.

### Function Contract
**Inputs**

- `n`: An integer representing the total number of nodes in the complete binary tree. `n` is always of the form `2^k - 1` for some integer `k >= 1`.
- `cost`: A list of integers of length `n`, where `cost[i]` is the initial value of the `i`-th node.

**Return value**

- An integer, representing the minimum total cost that needs to be added to nodes to make all root-to-leaf path sums equal.

### Examples
**Example 1**

- Input: `n = 7`, `cost = [1, 5, 2, 2, 3, 3, 1]`
- Output: `6`
- Explanation:
    The tree structure is:
    ```
            1 (idx 0)
           / \
          5(idx 1)  2(idx 2)
         / \       / \
        2(idx 3) 3(idx 4) 3(idx 5) 1(idx 6)
    ```
    We process nodes from the deepest parents upwards.
    1.  **Node 2 (cost 2):** Children are Node 5 (cost 3) and Node 6 (cost 1).
        *   Path sum from Node 2 through Node 5: `cost[5] = 3`.
        *   Path sum from Node 2 through Node 6: `cost[6] = 1`.
        *   Max child path sum: `max(3, 1) = 3`.
        *   To equalize, add `(3 - 3) = 0` to Node 5's path and `(3 - 1) = 2` to Node 6's path.
        *   `total_added_cost = 0 + 2 = 2`.
        *   Update `cost[2]` to reflect the max path sum from its subtree: `cost[2] = 2 + 3 = 5`. (Effectively, `cost` array becomes `[1, 5, 5, 2, 3, 3, 1]`)
    2.  **Node 1 (cost 5):** Children are Node 3 (cost 2) and Node 4 (cost 3).
        *   Path sum from Node 1 through Node 3: `cost[3] = 2`.
        *   Path sum from Node 1 through Node 4: `cost[4] = 3`.
        *   Max child path sum: `max(2, 3) = 3`.
        *   To equalize, add `(3 - 2) = 1` to Node 3's path and `(3 - 3) = 0` to Node 4's path.
        *   `total_added_cost = 2 + 1 + 0 = 3`.
        *   Update `cost[1]` to reflect the max path sum from its subtree: `cost[1] = 5 + 3 = 8`. (Effectively, `cost` array becomes `[1, 8, 5, 2, 3, 3, 1]`)
    3.  **Node 0 (cost 1):** Children are Node 1 (effective path sum 8) and Node 2 (effective path sum 5).
        *   Path sum from Node 0 through Node 1: `cost[1] = 8`.
        *   Path sum from Node 0 through Node 2: `cost[2] = 5`.
        *   Max child path sum: `max(8, 5) = 8`.
        *   To equalize, add `(8 - 8) = 0` to Node 1's path and `(8 - 5) = 3` to Node 2's path.
        *   `total_added_cost = 3 + 0 + 3 = 6`.
        *   Update `cost[0]` to reflect the max path sum from its subtree: `cost[0] = 1 + 8 = 9`. (Effectively, `cost` array becomes `[9, 8, 5, 2, 3, 3, 1]`)
    The final `total_added_cost` is 6.

**Example 2**

- Input: `n = 3`, `cost = [1, 2, 3]`
- Output: `1`
- Explanation:
    Tree:
    ```
        1 (idx 0)
       / \
      2(idx 1) 3(idx 2)
    ```
    1.  **Node 0 (cost 1):** Children are Node 1 (cost 2) and Node 2 (cost 3).
        *   Path sum from Node 0 through Node 1: `cost[1] = 2`.
        *   Path sum from Node 0 through Node 2: `cost[2] = 3`.
        *   Max child path sum: `max(2, 3) = 3`.
        *   To equalize, add `(3 - 2) = 1` to Node 1's path and `(3 - 3) = 0` to Node 2's path.
        *   `total_added_cost = 1 + 0 = 1`.
        *   Update `cost[0]` to reflect the max path sum from its subtree: `cost[0] = 1 + 3 = 4`.
    The final `total_added_cost` is 1.

**Example 3**

- Input: `n = 1`, `cost = [100]`
- Output: `0`
- Explanation: A single node tree has no paths to equalize. No cost needs to be added.

---

## Underlying Base Algorithm(s)
This problem can be efficiently solved using a **Dynamic Programming** approach combined with a **Greedy** strategy.
1.  **Bottom-Up Traversal:** The solution processes the tree from the deepest parent nodes upwards towards the root. This is characteristic of bottom-up dynamic programming on trees, where the results from children subtrees are used to compute values for their parents.
2.  **Greedy Choice:** At each parent node, to minimize the total added cost, we must ensure that the maximum path sum from its left child's subtree equals the maximum path sum from its right child's subtree. This is achieved by identifying the larger of the two child path sums and adding the difference to the smaller one. This local greedy choice contributes to the global minimum because any other choice (e.g., making both equal to something less than the maximum, or making them unequal) would either require more additions or fail to equalize paths.
3.  **Array Representation:** The complete binary tree is conveniently represented as an array, allowing direct access to children nodes using simple arithmetic (`2*i + 1` and `2*i + 2`). The `cost` array is modified in-place to store the maximum path sum from a node to any leaf in its subtree, effectively memoizing subproblem results.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
    The algorithm iterates through the parent nodes of the tree. In a complete binary tree with `n` nodes, there are `n/2` parent nodes (from index `n/2 - 1` down to `0`). Each iteration involves a constant number of operations (array lookups, comparisons, additions). Therefore, the total time complexity is proportional to the number of nodes, `O(n)`.
- **Space Complexity**: `O(1)` (Auxiliary Space)
    The algorithm modifies the input `cost` array in place. It uses only a few additional variables to store `total_added_cost`, child indices, and child costs. This auxiliary space requirement is constant, `O(1)`. If the input array itself is considered part of the space complexity, then it would be `O(n)`.
