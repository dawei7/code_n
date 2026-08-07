## General
### Beginner-Friendly Intuition & Strategy
The core task in **Index Pairs of a String** is to a string `text` and an array of strings `words`, return *an array of all index pairs *`[i, j]`* so that the substring *`text[i...j]`* is in `words`*. The data is structured as a **Binary Tree** where each node contains a value (`val`) and pointers to its `left` and `right` children. Instead of treating the tree as an array, the algorithm uses **Tree Traversal (Recursion / DFS)** to process each node and its subtrees. At every node, it recursively compares or transforms the left and right child subtrees, combining their results to solve the problem for the entire tree.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We check the base conditions for tree nodes. If a tree node is `None` (empty), we return the base boundary value (e.g., `True` for equality or `0` for depth).  
**Step 2: Core Processing & Traversal**  
1. Inspect the current node values (e.g. `p.val` and `q.val`).  
2. If values differ, return `False` immediately.  
3. Recursively invoke traversal on left child subtrees (`self.isSameTree(p.left, q.left)`).  
4. Recursively invoke traversal on right child subtrees (`self.isSameTree(p.right, q.right)`).  
5. Return `True` only if both left and right subtrees match.  
**Step 3: Completion & Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Both Nodes Empty (`None`):** Returns `True` as two empty subtrees are identical.
- **One Node Empty, One Non-Empty:** Returns `False` immediately, preventing null pointer attribute access (`AttributeError`).


## Complexity detail
- **Time Complexity**: $O(S+NL)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(S)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
