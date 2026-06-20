# Binary Tree Maximum Path Sum

| | |
|---|---|
| **ID** | `tree_10` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) |

## Problem statement

Given the `root` of a binary tree, return the **maximum path sum** of any non-empty path.
A path is defined as any sequence of adjacent nodes (connected by edges). The path may start and end at ANY node in the tree. It does not need to pass through the root.
A path sum is the sum of the node's values in the path.

**Input:** A binary tree `root` node.
**Output:** An integer representing the maximum path sum.

## When to use it

- The absolute hardest "standard" binary tree problem you will face in a FAANG interview.
- A brilliant test of Bottom-Up Post-Order DFS combined with negative number pruning.

## Approach

**1. The "Arch" vs "Branch" Problem:**
This problem is mathematically identical to finding the **Diameter of a Tree (`tree_07`)**. The maximum path looks like a giant "Arch" spanning from some left-side node, going UP to a connecting root, and DOWN to some right-side node.
For any arbitrary node, the maximum arch going *through* it is: `(Max path going down Left) + (Node Value) + (Max path going down Right)`.
However, when a node returns a value back UP to its parent, it CANNOT return an Arch! A path cannot branch in 3 directions! It can only return a straight line (a "Branch"). The parent must choose whether to connect to the left branch OR the right branch!

**2. The Bottom-Up Recursion:**
We write a recursive DFS function that returns the Maximum "Straight Line Branch" going down from a node.
- `left_branch = dfs(node.left)`
- `right_branch = dfs(node.right)`
What does this node return to its parent? It returns `node.val + max(left_branch, right_branch)`.

**3. The Global "Arch" Calculation:**
While calculating those branches, what is the maximum "Arch" that can physically pass completely THROUGH this node?
It is `left_branch + node.val + right_branch`!
We calculate this Arch value at every single node, and update a global `max_sum` variable!

**4. The Negative Number Trap:**
What if `left_branch` is `-50`? If we add `-50` to our Arch or our returned Branch, we are strictly making our sum WORSE!
Unlike the Diameter problem (which counts edges), this problem uses node values, which can be negative!
If a child returns a negative path, we simply IGNORE IT! We act as if the branch doesn't exist. We "prune" it by taking `max(0, branch_sum)`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_10: Max Path Sum.

Max root-to-leaf path sum (non-negative values).
"""


def solve(children, values, root, n):
    best = 0

    def walk(u):
        nonlocal best
        if not children[u]:
            if values[u] > best:
                best = values[u]
            return values[u]
        child_sums = [walk(v) for v in children[u]]
        s = values[u] + max(child_sums)
        if s > best:
            best = s
        return s

    walk(root)
    return best
```

</details>

## Walk-through

Tree:
```text
     -10
     /  \
    9   20
       /  \
      15   7
```

1. **`dfs(15)`:**
   - Left null (0), Right null (0).
   - `local_arch_sum = 0 + 15 + 0 = 15`. `max_sum = 15`.
   - Returns: `15 + max(0, 0) = 15`.
2. **`dfs(7)`:**
   - Left null (0), Right null (0).
   - `local_arch_sum = 0 + 7 + 0 = 7`. `max_sum = max(15, 7) = 15`.
   - Returns: `7 + max(0, 0) = 7`.
3. **`dfs(20)`:**
   - Left branch is 15. Right branch is 7.
   - `local_arch_sum = 15 + 20 + 7 = 42`. `max_sum = max(15, 42) = 42`.
   - Returns: `20 + max(15, 7) = 35`. *(It tells its parent: "If you connect to me, the best path down is 35")*.
4. **`dfs(9)`:**
   - Left null (0), Right null (0).
   - `local_arch_sum = 9`. `max_sum = 42`.
   - Returns: `9`.
5. **`dfs(-10)` (Root):**
   - Left branch is 9. Right branch is 35.
   - `local_arch_sum = 9 + (-10) + 35 = 34`. `max_sum = max(42, 34) = 42`.
   - Returns: `-10 + max(9, 35) = 25`.

Recursion ends. Return `max_sum = 42`. ✓
*(The path is `15 -> 20 -> 7`)*.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The DFS traversal visits every single node exactly once. Doing $O(1)$ constant time addition and `max()` operations at each node.
Time complexity is exactly $O(N)$.
Space complexity is bounded by the recursive call stack, which equals the height of the tree $O(H)$. In the average/best case (balanced tree), space is $O(\log N)$. In the worst case (skewed tree), it degrades to $O(N)$.

## Variants & optimizations

- **Kadane's Algorithm for Arrays (`dynamic_04`):** This tree problem is actually a direct, topological evolution of finding the Maximum Subarray Sum in a 1D Array! The logic of `max(0, branch)` is the exact same logic as "reset the running sum to 0 if it goes negative".

## Real-world applications

- **Supply Chain Logistics:** Finding the most profitable continuous transportation route across a heavily branching distribution network, where some nodes (tolls/taxes) have negative values and others (cities) have positive profits.

## Related algorithms in cOde(n)

- **[tree_07 - Tree Diameter](tree_07_tree-diameter.md)** — The exact same architectural approach, but counting physical edges instead of summing values.
- **[dynamic_04 - Kadane's Algorithm](../dynamic/dp_04_maximum-subarray.md)** — The 1D array equivalent of this problem.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
